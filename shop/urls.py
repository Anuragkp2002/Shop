"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from user import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('registerAction/',views.registerAction,name="registerAction"),
    path('login/',views.login,name="login"),
    path('loginAction/',views.loginAction,name="loginAction"),
    path('viewuser/',views.viewuser,name="viewuser"),
    path('delete<int:id>/',views.delete,name='delete'),
    path('edit<int:id>)/',views.edit,name="edit"),
    path('editAction/',views.editAction,name="editAction"),
    path('imageupload/',views.imageupload,name="imageupload"),
    path('imageAction/',views.imageAction,name="imageAction"),
    path('viewimage/',views.viewimage,name="viewimage"),
    path('dropdownbinding/',views.dropdownbinding,name="dropdownbinding"),
    path('getstate/',views.getstate,name="getstate"),
    path('jquerylink/',views.jquerylink,name="jquerylink"),
    path('educationdetails/',views.educationdetails,name="educationdetails")
    
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
