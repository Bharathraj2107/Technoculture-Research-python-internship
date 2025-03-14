# from django.contrib import admin
# from django.urls import path
# from django.views.generic import TemplateView
# from .views import index

# urlpatterns = [
#     path('admin/', admin.site.urls),
    
#     path('', TemplateView.as_view(template_name="index.html"), name="home"),  # Serve frontend
    


# ]
from django.contrib import admin
from django.urls import path
from expenses.views import index  # Import the index view from the expenses app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Set the root URL to load the index page
]

