from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from studentapp import views

urlpatterns = [
    path('addmarks/', views.post_data.as_view()),
    path('displaymark/', views.displaymark.as_view()),
    path('displaymarklist/',views.displaymarklist.as_view())
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
