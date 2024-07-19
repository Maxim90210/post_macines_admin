from django.urls import path
from views import locker_detail

urlpatterns = [
    path('locker/<int:locker_id>/', locker_detail, name='locker_detail'),
]


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lockers/', include('lockers.urls')),
]
