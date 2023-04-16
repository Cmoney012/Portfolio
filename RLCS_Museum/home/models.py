from django.db import models

class Series_Info(models.Model):
	series_id = models.IntegerField(null=True, blank=True)
	title = models.CharField(max_length=100)
	team_one = models.CharField(max_length=100, default='')
	team_one_logo = models.ImageField(upload_to='images/', default='images/default.jpg')
	team_one_score = models.IntegerField(default='0')
	team_two = models.CharField(max_length=100, default='')
	team_two_logo = models.ImageField(upload_to='images/', default='images/default.jpg')
	team_two_score = models.IntegerField(default='0')
	event = models.CharField(max_length=100)
	date_of_event = models.DateField()
	pregame = models.TextField(default='')
	game1 = models.TextField(default='')
	game2 = models.TextField(default='')
	game3 = models.TextField(default='')
	game4 = models.TextField(default='')
	game5 = models.TextField(default='')
	game6 = models.TextField(default='')
	postgame = models.TextField(default='')


	def __str__(self):
		return self.title

class Player_Info(models.Model):
	player_id = models.IntegerField()
	rank = models.IntegerField()
	name = models.CharField(max_length=100)
	birthday = models.DateField()
	championships = models.IntegerField()
	notable_teams = models.CharField(max_length=100)
	blurb = models.TextField()

	def __str__(self):
		return self.name

class Team_Info(models.Model):
	team_id = models.IntegerField()
	rank = models.IntegerField()
	name = models.CharField(max_length=100)
	championships = models.IntegerField()
	major_wins = models.IntegerField(default=0)
	regional_wins = models.IntegerField(default=0)	
	founded_date = models.DateField()
	notable_players = models.CharField(max_length=100)
	blurb = models.TextField()
	logo = models.ImageField(upload_to='images/', default='images/default.jpg')

	def __str__(self):
		return self.name