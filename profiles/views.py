from django.shortcuts import render

# Create your views here.
def member_profile(request, username):
    return render(request, 'member_profile.html',{'username':username})