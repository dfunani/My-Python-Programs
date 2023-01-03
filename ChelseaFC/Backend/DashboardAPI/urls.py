from django.urls import path
from DashboardAPI import views
urlpatterns = [
    path('clubs/<int:pk>/', views.GetClub.as_view()),
    path('clubs/', views.GetClubList.as_view())
]
