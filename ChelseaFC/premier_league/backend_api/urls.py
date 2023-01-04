from django.urls import path
from .views import ClubsViewSet, ClubFixturesView, ClubResultsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('clubs/', ClubsViewSet.as_view()),
    path('club/results/<int:pk>/', ClubResultsView.as_view()),
    path('club/fixtures/<int:pk>/', ClubFixturesView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
