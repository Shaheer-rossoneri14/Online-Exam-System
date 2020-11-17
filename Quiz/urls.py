from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('question/<int:subject_id>/', views.question, name='question'),
    path('logout/', views.log, name='log'),

]