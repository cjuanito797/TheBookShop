from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.urls'))
]
