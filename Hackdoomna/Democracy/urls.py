from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('signin', views.signin, name='Signin'),
    path('signup', views.signupview, name='Signup'),
    path('aboutus', views.aboutus, name='About'),
    path('services', views.Services, name='Services'),
    path('blog', views.blog, name='Blog'),
    path('contact', views.contact, name='Contact'),
    path('login', views.auth_login, name='Login'),
    path('register', views.register, name='Register'),
    path('voting', views.voting, name='Voting'),
    path('response', views.save_response, name='response'),
]
