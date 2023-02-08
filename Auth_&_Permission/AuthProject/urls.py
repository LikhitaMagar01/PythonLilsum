from django.contrib import admin
from django.urls import path, include
# from api import views
# from api2 import views
# from customPermission import views
from TokenAuth import views
from rest_framework.routers import DefaultRouter

# to ask/create token from client
from rest_framework.authtoken.views import obtain_auth_token

from TokenAuth.auth import CustomAuthToken

# api route
# router = DefaultRouter()
# router.register('studentapi', views.StudentModelViewSet, basename='student')
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
# ]

# api2 route
# router = DefaultRouter()

# router.register('workerapi', views.WorkerModelViewSet, basename='worker')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# custom permission route
# router = DefaultRouter()

# router.register('custompermissionapi', views.WorkerModelViewSet, basename='worker')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# TokenAuth
router = DefaultRouter()

router.register('tokenApi', views.WorkerModelViewSet, basename='worker')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', obtain_auth_token),
    # cutom token from auth
    path('gettoken/', CustomAuthToken.as_view())
]