from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from home import urls as url_home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include(url_home)),
    path('clientes/', include(clientes_urls)),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('admin/', admin.site.urls),
]
