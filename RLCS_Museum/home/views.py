from django.shortcuts import render, get_object_or_404
from .models import Series_Info, Player_Info, Team_Info
from django.http import HttpResponse
from collections import Counter
from octanegg import Octane
from itertools import chain
import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
from .utils import get_stats, update_stats_per_game



def home(request):

    series_info = Series_Info.objects.all()
    series_id = request.GET.get('series_id')
    if series_id:
        series = get_object_or_404(Series_Info, pk=series_id)
    else:
        series = None
    context = {
        'Series_Info': series_info,
        'series': series
    }
    return render(request, 'home/home.html', context)

def scoreboard_detail(request, series_id):
    series = get_object_or_404(Series_Info, pk=series_id)
    context = {'series': series}
    return render(request, 'home/scoreboard_detail.html', context)

def series(request):
    series = Series_Info.objects.all()
    context = {
        'series': series
    }
    return render(request, 'home/series/series-home.html', context)

def series_logo1(request):
    logo = 'home/series/static/images/IBP.jpg'
    context = [
        logo
    ]
    return render(request, 'home/series/series-home.html', context)

def teams(request):
    teams = Team_Info.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'home/teams/teams-home.html', context)

def players(request):
    players = Player_Info.objects.all()
    context = {
        'players': players
    }
    return render(request, 'home/players/players-home.html', context)

def display_data(request):
    print("Display data view function called")
    try:
        with Octane() as client:
            time_period = int(request.POST.get('time-period', 1))  # default to 1 month
            after_date = (datetime.now() - relativedelta(months=time_period)).strftime('%Y-%m-%d')
            before_date = datetime.now().strftime('%Y-%m-%d')
            games = []
            goals = 0
            page = 1
            while True:
                current_page_games = client.get_games(tier='S', after=after_date, before=before_date, page=page)
                if not current_page_games:  # no more games
                    break
                games += current_page_games
                page += 1
                print(page)
                #print(current_page_games)
            num_games = len(games)
            blue_players = [player.get('player').get('tag') for game in games for player in game.get('blue').get('players')]
            orange_players = [player.get('player').get('tag') for game in games for player in game.get('orange').get('players')]
            players = blue_players + orange_players
            player_counts = Counter(players)
            most_common_players = [{'tag': tag, 'count': count} for tag, count in player_counts.most_common(15)]
            player_goals = [{player.get('player').get('tag'): player.get('stats').get('core').get('goals')} for player in most_common_players if player.get('player') is not None]
            return render(request, 'home/data.html', {'player_goals': player_goals, 'num_games': num_games, 'most_common_players': most_common_players})

    except Exception as e:
        logging.exception('An error occurred while fetching data from the Octane API')
        return render(request, 'home/error.html', {'error_message': 'An error occurred while fetching data from the Octane API. Please try again later.'})


def stats(request):
    start_date = request.POST.get('start-date', '2020-01-01')
    end_date = request.POST.get('end-date', '2023-03-22')
    per_game = request.POST.get('per_game_checkbox', False)
    sort_by = request.POST.get('sort-by', 'games')
    minimum_games = request.POST.get('minimum-games', 0)
    stats = get_stats(after_date=start_date, before_date=end_date, per_game=per_game, sort_by=sort_by, minimum_games=minimum_games)
    context = {
        'start_date': start_date,
        'end_date': end_date,
        'per_game': per_game,
        'sort_by': sort_by,
        'minimum_games': minimum_games,
        'stats': stats,
    }
    return render(request, 'home/stats.html', {'context': context})
