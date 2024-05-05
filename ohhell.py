from collections import defaultdict
from dataclasses import dataclass
from typing import List



DECK_SIZE = 54
with open("VERSION") as file:
    GAME_VERSION = file.read()
SCORE_MULTIPLIER = 10



@dataclass
class Player:
    name: str
    score: int
    bids: int
    wins: int



def enter_players(num_players: int):
    players = []
    for i in range(num_players):
        players.append(
            Player(str(input("Enter the player's name: ")), 0, 0, 0)
        )
    print("=====================================")
    return players


def enter_player_guesses(players: List[Player], round: int):
    total_bids = 0
    allowed_bids = round + 1
    for i in range(len(players)):
        player = players[(i + round) % len(players)]
        if i == len(players) - 1 and total_bids <= allowed_bids:
            print(f"The next player CANNOT GUESS {allowed_bids - total_bids}")
        player.bids = int(input(f"How many tricks will {player.name} win?: "))
        total_bids += player.bids


def enter_tricks_won(players: List[Player], round: int):
    for i in range(len(players)):
        player = players[(i+round) % len(players)]
        player.wins = int(input(f"How many tricks did {player.name} win?: "))


def update_scores(players: List[Player]):
    print("Current Scores")
    for player in players:
        if player.bids != player.wins:
            player.score -= abs(player.wins - player.bids) * 10
        else:
            player.score += 20 + (10 * player.bids)
        print(f"{player.name}: {player.score} points")

def display_winner(players: List[Player]):
    players.sort(key=lambda x:x.score, reverse=True)
    print(f"The winner is {players[0].name}! They scored {players[0].score} points!")


def game_loop(players: List[Player], max_rounds: int):
    for round in range(max_rounds):
        print(f"Round {round+1}")
        enter_player_guesses(players, round)
        print("------------------")
        enter_tricks_won(players, round)
        print("------------------")
        update_scores(players)
        print("=====================================")

    display_winner(players)


def main():
    print(f"Oh Hell! v{GAME_VERSION}")
    ## Ask for player inputs
    num_players = int(input("How many people will play? (Min: 3, Max: 10) "))
    if num_players < 3 or num_players > 10:
        raise ValueError("The number of people who want to play is not possible")
    
    ## Initialize game variables
    players = enter_players(num_players)
    max_rounds = (DECK_SIZE-1)//num_players

    ## Run the game
    game_loop(players, max_rounds)


if __name__ == "__main__":
    main()