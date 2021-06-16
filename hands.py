from player_one import Player_one
from player_two import Player_two
from computer import Computer

class Hands:
    def __init__(self):
        self.player_one = Player_one()
        self.player_two = Player_two()
        self.player_two = Computer()


    def run_game(self):
        self.display_welcome()
        self.display_instructions()
        self.choose_one_or_two_player_mode()
        self.game_rounds()
        self.display_winner()


    def display_welcome(self):
        print("Welcome to Rocks, Paper, Scissors, Lizards, Spock!")

    def display_instructions(self):
        print("instructions:")
        print("scissors cuts paper")
        print("paper covers rock")
        print("rock crushes lizard")
        print("lizard poisons Spock")
        print("Spock smashes scissors")
        print("scissors kill lizard")
        print("lizard eats paper")
        print("paper disproves Spock")
        print("Spock vaporizes rock")
        print("rock crushes scissors")

    def choose_one_or_two_player_mode(self):
        user_input = input("choose your opponent: computer or player two")
        if user_input == "player two":
            self.player_two = Player_two()
        elif user_input == "computer":
            self.player_two = Computer()

    def game_rounds(self):
        self.show_player_one_options()
        self.show_player_two_options()
        pass

    def player_one_turn(self):
        print("rock, paper, scissors, lizard, SPOCK!!!")
        gesture_one_input = (input())

    def player_two_turn(self):
        print("rock, paper, scissors, lizard, SPOCK!!!")
        gesture_two_input = (input())

    def show_player_one_options(self):
        gesture_index = 0
        for gesture in self.player_one.gestures:
            print(f"press {gesture_index} for {gesture}")
            gesture_index += 1

    def show_player_two_options(self):
        gesture_index = 0
        for gesture in self.player_two.gestures:
            print(f"press {gesture_index} for {gesture}")
            gesture_index += 1


    def test_score(self):
        self.player_one.score += 1

    def display_winner(self):
        print("player one's score is "f"{self.player_one.score}")
        print("player two's score is "f"{self.player_two.score}")
