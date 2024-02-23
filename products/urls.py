from django.urls import path,include
from rest_framework.routers import  DefaultRouter
from . import views
router = DefaultRouter()
router.register('all', views.productView)
router.register('review', views.reviewViewset)
router.register('wishlist', views.wishlistViewset)
urlpatterns = [
    path('', include(router.urls)),   
]
