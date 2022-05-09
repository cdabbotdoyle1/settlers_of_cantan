from matplotlib.font_manager import json_dump


class GameStatistics(object):
    def __init__(self,id,first_player,second_player):
        self.id = id
        self.first_player = first_player
        self.second_player = second_player


def compute_leaderboard():
    # Current Fetch Player Stats from DB
    return json_dump