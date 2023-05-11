from django.urls import include, path
from rest_framework import routers
from authentication.views import UserViewSet
from restaurant.views import RestaurantViewSet
from menu.views import MenuViewSet, TodayMenuViewSet, WinnerMenuViewSet
from vote.views import VoteViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'restaurant', RestaurantViewSet)
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'vote', VoteViewSet)

router.register(r'today_menu', TodayMenuViewSet, basename='today_menu')
router.register(r'winner_menu', WinnerMenuViewSet, basename='winner_menu')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
