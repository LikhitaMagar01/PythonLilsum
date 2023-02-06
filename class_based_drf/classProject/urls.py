from django.contrib import admin
from django.urls import path, include
# from api import views
# from student import views
# from concreteAPI import views
# from viewSet import views
# from modelViewSet import views
from ReadOnlyModelView import views
from rest_framework.routers import DefaultRouter
# api app
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('studentapi/', views.StudentAPI.as_view()),
#     path('studentapi/<int:pk>', views.StudentAPI.as_view()),
# ]

# urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('kidsapi/', views.KidsList.as_view()),
    # path('kidsapi/', views.KidsCreate.as_view()),
    # path('kidsapi/<int:pk>', views.KidsRetrieve.as_view())
    # path('kidsapi/<int:pk>', views.KidsUpdate.as_view())
    # path('kidsapi/<int:pk>', views.KidsDelete.as_view())
    # path('kidsapi/', views.listCreateAPI.as_view()),
    # path('kidsapi/<int:pk>', views.RetrieveUpdateDelete.as_view())
# ]

# concreate
# urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('memberapi/', views.MemberList.as_view()),
    # path('memberapi/', views.MemberCreate.as_view()),
    # path('memberapi/<int:pk>', views.MemberRetrieve.as_view()),
    # path('memberapi/', views.MemberUpdate.as_view()),
    # path('memberapi/', views.MemberDestroy.as_view()),
    # path('memberapi/', views.MemberListCreate.as_view()),
    # path('memberapi/', views.MemberRetrieveUpdate.as_view()),
    # path('memberapi/', views.MemberRetrieveDestroy.as_view()),
    # path('memberapi/', views.MemberRetrieveUpdateDestroy.as_view()),
#     path('studentapi/<int:pk>', views.StudentAPI.as_view()),
# ]

# ViewSet
# Creating Router Object
router = DefaultRouter()

# Register FamilyViewSet with Router
# router.register('studentapi', views.FamilyViewSet, basename='student')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
# ]

# Register WorkerModelViewSet with Router
# router.register('workerapi', views.WorkerModelViewSet, basename='worker')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
# ]

# Register readonlyviewset with router
router.register('workerapi', views.ReadOnlyWorkerViewSet, basename='worker')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]