
from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('users',views.userViewSet)
urlpatterns = [  
    path('',include(router.urls)),
    path('register/', views.registerView.as_view(), name='register'),
    path('login/', views.loginView.as_view(), name='login'),
    path('logout/', views.logOutView.as_view(), name='logout'),
    path('activate/<uid64>/<token>/', views.activate, name='activate'),
]
