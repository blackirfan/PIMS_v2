from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from model import AuthUser


@login_required
def home(request):

    return render(request, "home.html", {})
