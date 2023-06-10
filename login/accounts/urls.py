from django.contrib import admin
from django.urls import path
from .views import *
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import  MyPasswordChangeForm,  MyPasswordResetForm, MySetPasswordForm
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('' ,  home  , name="home"),
    path('register' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('passwordchange/',auth_middleware( auth_views.PasswordChangeView
         .as_view(template_name='passwordchange.html',
         form_class=MyPasswordChangeForm,success_url='/passwordchangedone/')), name='passwordchange'),
    path('passwordchangedone/',auth_middleware( auth_views.PasswordChangeView.
         as_view(template_name='passwordchangedone.html')),
         name='passwordchangedone'),
    path('profile/',auth_middleware( views.ProfileView.as_view()), name='profile'),
    path('address/',auth_middleware( views.address), name='address'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/?next=/'),name='logout'),

     path('password-reset/', auth_views.PasswordResetView.
         as_view(template_name='password_reset.html',
          form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.
         as_view(template_name='password_reset_done.html',
          ),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.
         as_view(template_name='password_reset_confirm.html',
          form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.
         as_view(template_name='password_reset_complete.html'),
          name='password_reset_complete'),
    
   
]+ static(settings.MEDIA_URL, document_root=settings.
MEDIA_ROOT)