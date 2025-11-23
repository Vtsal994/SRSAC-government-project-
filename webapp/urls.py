from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Homepage
    path('about.html', views.about, name='about'), # About Us page (as you had it in the first working version)
    path('applications.html', views.applications, name='applications_html'), # Add this line
    path('applications/', views.applications, name='applications'), # Keep this for the clean URL
]