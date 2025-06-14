from django.http import JsonResponse


def auth_status(request):
    if request.user.is_authenticated:
        return JsonResponse(
            {
                "authenticated": True,
                "username": request.user.username,
                "email": request.user.email,
            }
        )
    return JsonResponse({"authenticated": False})
