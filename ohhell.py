from __future__ import annotations


DECK_SIZE = 52
SCORE_MULTIPLIER = 10
with open("VERSION") as file:
    GAME_VERSION = file.read()


class Player:
    name: str
    bids: list[int]
    wins: list[int]

    def __init__(self, player_name: str):
        self.name = player_name
        self.bids = []
        self.wins = []

    def record_bids(self):
        player_bid = int(input(f"How many tricks will {self.name} win?: "))
        self.bids.append(player_bid)

    def record_wins(self):
        player_win = int(input(f"How many tricks did {self.name} win?: "))
        self.wins.append(player_win)

    @property
    def score(self):
        score = 0
        for bid, win in zip(self.bids, self.wins):
            score += self._compute_score(bid, win)
        return score

    def _compute_score(self, bid: int, win: int) -> int:
        if bid != win:
            return abs(win - bid) * -10
        return 20 + (10 * bid)



def enter_players(num_players: int):
    players = []
    for i in range(num_players):
        players.append(
            Player(str(input(f"Enter a name for player #{i+1}: ")).lower())
        )
    print("=====================================")
    return players


def enter_player_guesses(players: list[Player], round: int):
    total_bids = 0
    allowed_bids = round + 1
    for i in range(len(players)):
        player = players[(i + round) % len(players)]
        if i == len(players) - 1 and total_bids <= allowed_bids:
            print(f"The next player CANNOT GUESS {allowed_bids - total_bids}")
        player.record_bids()
        total_bids += player.bids[-1]

def enter_tricks_won(players: list[Player], round: int):
    for i in range(len(players)):
        player = players[(i+round) % len(players)]
        player.record_wins()


def update_scores(players: list[Player]) -> list:
    print("Current Scores")
    player_scores = []
    for player in players:
        player_scores.append((player.name, player.score))

    # print the scores in order after each round
    for pair in sorted(player_scores, key=lambda x:x[1], reverse=True):
        print(f"{pair[0]}: {pair[1]} points")
    
    return player_scores


def display_winner(current_scores: list[tuple[Player, int]]):
    current_scores.sort(key=lambda x:x[1], reverse=True)
    print(f"The winner is {current_scores[0][0]}! They scored {current_scores[0][1]} points!")
    print(f"The runner up is {current_scores[1][0]}! They scored {current_scores[1][1]} points!")
    print(f"And in third place is {current_scores[2][0]}! They scored {current_scores[2][1]} points!")


def game_loop(players: list[Player], max_rounds: int):
    current_scores = []
    for round in range(max_rounds):
        print(f"Round {round+1}")
        enter_player_guesses(players, round)
        print("------------------")
        enter_tricks_won(players, round)
        print("------------------")
        current_scores = update_scores(players)
        print("=====================================")

    display_winner(current_scores)


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