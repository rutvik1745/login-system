from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if not request.user.is_authenticated:
                return redirect('/accounts/login/?next=/')
        response = get_response(request)
        return response
    return middleware
