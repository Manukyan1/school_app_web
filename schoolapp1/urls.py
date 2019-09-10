from django.urls import path, include
from .views import *
from django.views.defaults import server_error, page_not_found, permission_denied
urlpatterns = [
    path('', main_func),
    path('homepage/', home_func, name='homep'),
    path('reg/', reg_func, name='regp'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', profile_func)
]
