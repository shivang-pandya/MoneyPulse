from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # index.html
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),

]