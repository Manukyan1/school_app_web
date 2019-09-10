from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext


def main_func(request):
    return render(request, 'schoolapp1/index.html')





def reg_func(request):
    fnamev = request.POST['fnamef']
    lnamev = request.POST['lnamef']
    emailv = request.POST['emailf']
    passv = request.POST['passwordf']
    repassv = request.POST['reppasswordf']
    reg_info = [fnamev, lnamev, emailv, passv, repassv]
    return render(request, 'schoolapp1/regt.html', context={'reg_infok': reg_info})




def home_func(request):
    return render(request, 'schoolapp1/homet.html')





def profile_func(request):
    auth = request.user.is_authenticated
    group = request.user.groups.all()
    return render(request, 'schoolapp1/profilet.html', context={'username': request.user.username, 'group': group})





def handler404(request, exception, template_name="errs/404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response
