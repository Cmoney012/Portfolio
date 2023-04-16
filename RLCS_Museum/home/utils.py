import requests
import json
import datetime


def get_stats(sort_by, minimum_games, after_date=None, before_date=None, per_game=False):
    page = 1
    player_stats = {}
    while True:
        response = requests.get("https://zsr.octane.gg/matches?mode=3&tbd=false&tier=S" + f"&after={after_date}" + f"&before={before_date}" + f"&page={page}")
        data = json.loads(response.text)

        if len(data["matches"]) == 0:
            break

        for match in data["matches"]:
            if "games" in match:
                match_length = len(match["games"])
            else:
                match_length = 0
            event_name = match["event"]["name"]
            
            if "date" in match:
                try:
                    date = datetime.datetime.strptime(match["date"], "%Y-%m-%dT%H:%M:%SZ").strftime("%m-%d-%Y")
                except ValueError:
                    try:
                        date = datetime.datetime.strptime(match["date"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%m-%d-%Y")
                    except ValueError:
                        date = "Unknown"
            else:
                date = "Unknown"
            
            blue_name = match["blue"]["team"]["team"]["name"]
            orange_name = match["orange"]["team"]["team"]["name"]

            if "winner" in match["orange"] and match["orange"]["winner"]:
                winner = orange_name
            else:
                winner = blue_name
            if "score" in match["blue"]:
                blue_score = match["blue"]["score"]
            else:
                blue_score = 0
            if "score" in match["orange"]:
                orange_score = match["orange"]["score"]
            else:
                orange_score = 0

            blue_players = match["blue"].get("players", [])
            orange_players = match["orange"].get("players", [])

            for player in blue_players:
                name = player["player"]["tag"]
                
                if name not in player_stats:
                    player_stats[name] = {"info": {"country":""}, "stats": {"games": 0, "shots": 0, "goals": 0, "saves": 0, "assists": 0, "score": 0,
                                          "shootingPercentage": 0, "amountUsedWhileSupersonic":0, "avgSpeed": 0, "octrating": 0}}
                
                player_stats[name]["stats"]["games"] += match_length
                player_stats[name]["stats"]["shots"] += int(player["stats"]["core"]["shots"])
                player_stats[name]["stats"]["goals"] += int(player["stats"]["core"]["goals"])
                player_stats[name]["stats"]["saves"] += int(player["stats"]["core"]["saves"])
                player_stats[name]["stats"]["assists"] += int(player["stats"]["core"]["assists"])
                player_stats[name]["stats"]["score"] += float(player["stats"]["core"]["score"])
                player_stats[name]["stats"]["amountUsedWhileSupersonic"] += float(player["stats"]["boost"]["amountUsedWhileSupersonic"])
                player_stats[name]["stats"]["avgSpeed"] += float(player["stats"]["movement"]["avgSpeed"])
                player_stats[name]["stats"]["octrating"] += float(player["advanced"]["rating"])

            for player in orange_players:
                name = player["player"]["tag"]
               
                if name not in player_stats:
                    player_stats[name] = {"info": {"country": ""}, "stats": {"games": 0, "shots": 0, "goals": 0, "saves": 0, "assists": 0, "score": 0,
                                          "shootingPercentage": 0, "amountUsedWhileSupersonic": 0, "avgSpeed": 0, "octrating": 0}}
                
                player_stats[name]["stats"]["games"] += match_length
                player_stats[name]["stats"]["shots"] += int(player["stats"]["core"]["shots"])
                player_stats[name]["stats"]["goals"] += int(player["stats"]["core"]["goals"])
                player_stats[name]["stats"]["saves"] += int(player["stats"]["core"]["saves"])
                player_stats[name]["stats"]["assists"] += int(player["stats"]["core"]["assists"])
                player_stats[name]["stats"]["score"] += float(player["stats"]["core"]["score"])
                player_stats[name]["stats"]["amountUsedWhileSupersonic"] += float(player["stats"]["boost"]["amountUsedWhileSupersonic"])
                player_stats[name]["stats"]["avgSpeed"] += float(player["stats"]["movement"]["avgSpeed"])
                player_stats[name]["stats"]["octrating"] += float(player["advanced"]["rating"])

        page += 1
        print(page)

    if per_game:
        player_stats = update_stats_per_game(player_stats)

    player_stats = dict(sorted(player_stats.items(), key=lambda x: x[1]["stats"][sort_by], reverse=True))

    remove_list = []
    for name, stats in player_stats.items():
        if stats["stats"]["games"] < int(minimum_games):
            remove_list.append(name)

    for name in remove_list:
        player_stats.pop(name)

    num_players = len(player_stats)

    player_stats["average"] = {"info": {"country":""}, "stats": {"games": 0, "shots": 0, "goals": 0, "saves": 0, "assists": 0, "score": 0,
                                          "shootingPercentage": 0, "amountUsedWhileSupersonic":0, "avgSpeed": 0, "octrating": 0}}
    
    for player in player_stats:
        print(player)
        for stat in player["stats"].keys():
            print(stat)
            player_stats["average"]["stats"][stat] =  round(sum([player[stat] for player, stat in player_stats.items() if stat["stats"]["games"] > 0]))


    for name, stats in player_stats.items():
        if stats["stats"]["shots"] > 0:
            shooting_percentage = stats["stats"]["goals"] / stats["stats"]["shots"]
            stats["stats"]["shootingPercentage"] = "{:.2f}%".format(shooting_percentage * 100)
    else:
        stats["stats"]["shootingPercentage"] = None

    return player_stats


def update_stats_per_game(a):
    for name, player_dict in a.items():
        stats_dict = player_dict["stats"]
        games_played = stats_dict["games"]
        for key, value in stats_dict.items():
            if key not in ["games", "shootingPercentage"] and games_played > 0:
                try:
                    stats_dict[key] = round(float(value) / float(games_played), 2)
                except ValueError:
                    pass
    return a




#     {player_stats: {"GarretG": {"info": {"country": ""}}, {"stats": {"games": 0}, {"shots": 0}, {"goals": 0}, {"saves": 0}, {"assists": 0}, {"score": 0}, {"shootingPercentage": 0}, {"amountUsedWhileSupersonic": 0,}}} 