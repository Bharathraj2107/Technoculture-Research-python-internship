from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="home"),  # Serve frontend
    path('',lambda request:HttpResponse("Django is working!"))


]