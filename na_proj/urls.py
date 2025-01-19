from django.contrib import admin
from django.urls import path
from contest_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register_student, name='register'),
    path('submit-problem/', views.submit_problem, name='submit_problem'),
    path('register/', views.register_view, name="register" ),
    path('view-submissions/', views.list_submissions, name='list_submissions'),
    path('submit-solution/', views.solution_submissions, name='solution_submissions'),
    path('view-problems/', views.view_problems, name="view_problems"),

]
