from django.urls import path
from .views import ClubsViewSet, ClubFixturesView, ClubResultsView, standingsViewSet, clubStandingsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('clubs/', ClubsViewSet.as_view()),
    path('club/results/<int:pk>/', ClubResultsView.as_view()),
    path('club/fixtures/<int:pk>/', ClubFixturesView.as_view()),
    path('club/standings/<int:pk>/', clubStandingsView.as_view()),
    path('clubs/standings/', standingsViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
