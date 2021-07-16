"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from plat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # get and post req. for insert operation
    path('', views.user_form, name='user_insert'),
    # get and post req. for update operation
    path('<int:id>/', views.user_form, name='user_update'),
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
    # get req. to retrieve and display all records
    path('list/', views.user_list, name='user_list'),
    path('get-id', views.id, name='get_id')
]
