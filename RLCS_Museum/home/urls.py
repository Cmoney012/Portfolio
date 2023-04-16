from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home-home'),
	path('home/', views.home, name='home-home'),
	path('scoreboard/<int:series_id>/', views.scoreboard_detail, name='scoreboard_detail'),
	path('series/', views.series, name='series-home'),
	path('players/', views.players, name='players-home'),
	path('teams/', views.teams, name='teams-home'),
	path('data/', views.display_data, name='display_data'),
	path('stats/', views.stats, name='stats-home'),
]