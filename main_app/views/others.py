from django.shortcuts import render

from main_app.models import Profile


# def get_profile():
#     profiles = Profile.objects.all()
#     if profiles:
#         return profiles[0]
#     return None


def unauthorized(request):
    return render(request, '401_error.html')