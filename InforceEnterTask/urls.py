from django.urls import include, path
from rest_framework import routers
from authentication.views import UserViewSet
from restaurant.views import RestaurantViewSet
from menu.views import MenuViewSet
from vote.views import VoteViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'votes', VoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
