from collections import defaultdict
from dataclasses import dataclass

SCORE_MULTIPLIER = 10


@dataclass
class Player:
    name: str
    guesses: list[int]
    realized: list[int]

    @property
    def score(self):
        total_score = 0
        for guess, realized in zip(self.guesses, self.realized):
            total_score += self._compute_score(guess, realized)
        return total_score

    def get_guess(self):
        guess = int(input(f"What is {self.name}'s guess?"))
        self.guesses.append(guess)

    def get_realized(self):
        realized = int(input(f"What is {self.name}'s realized?"))
        self.realized.append(realized)

    def _compute_score(guess: int, actual: int) -> int:
        if guess == actual:
            return 10 if guess == 0 else guess * 10
        return abs(guess - actual) * -10


def main():
    estimates: dict[str, int] = defaultdict(int)
    actual: dict[str, int] = defaultdict(int)
    score: dict[str, int] = defaultdict(int)
    players = ["aarij", "ram", "sheev", "nawfal"]

    for round in range(12):
        print(f"Round {round+1}")
        for index in range(4):
            player = players[(index + round) % len(players)]
            estimates[player] = int(input(f"How many tricks will {player} win?: "))
        for index in range(4):
            player = players[(index + round) % len(players)]
            actual[player] = int(input(f"How many tricks did {player} win?: "))
            if estimates[player] == actual[player]:
                score[player] += 20 + (SCORE_MULTIPLIER * estimates[player])
            else:
                score[player] -= abs(estimates[player] - actual[player]) * 10
        print(score)
        print("-----------------------------------")


if __name__ == "__main__":
    main()


def test_round_two():
    pass
