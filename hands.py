
from player_one import Player_one
from player_two import Player_two
from computer import Computer

import random


class Hands:
    def __init__(self):
        self.player_one = Player_one()
        self.player_two = Player_two()
        self.computer = Computer()

    def run_game(self):
        self.display_welcome()
        self.display_instructions()
        self.choose_one_or_two_player_mode()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to Rocks, Paper, Scissors, Lizards, Spock!")

    def display_instructions(self):
        print("instructions:")
        print("rock crushes lizard")
        print("rock crushes scissors")
        print("paper disproves Spock")
        print("paper covers rock")
        print("scissors cuts paper")
        print("scissors kill lizard")
        print("lizard eats paper")
        print("lizard poisons Spock")
        print("Spock smashes scissors")
        print("Spock vaporizes rock")
        print("BEST TWO OUT OF THREE!")

    def choose_one_or_two_player_mode(self):
        user_input = input("choose your opponent: human or AI")
        if user_input == "human":
            self.two_player_mode()
        elif user_input == "AI":
            self.single_player_mode()
        elif user_input != "human" or "AI":
            print("incorrect input")
            self.choose_one_or_two_player_mode()

    def single_player_mode(self):# computer mode
        while self.player_one.score < 2 or self.player_two.score < 2:
            self.player_one_turn()
            self.computer_turn()
            self.the_referee()
            self.display_winner()

    def two_player_mode(self):# human mode
        while self.player_one.score < 2 or self.computer.score < 2:
            self.player_one_turn()
            self.player_two_turn()
            self.the_referee()
            self.display_winner()

    def the_referee(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("It's a tie, no points awarded.")
        elif self.player_one.chosen_gesture == self.computer.chosen_gesture:
            print("Its a tie, no points awarded.")
        elif self.player_two.chosen_gesture == 0 and self.player_one.chosen_gesture == 2:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.player_two.chosen_gesture == 0 and self.player_one.chosen_gesture == 3:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.player_two.chosen_gesture == 1 and self.player_one.chosen_gesture == 0:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.player_two.chosen_gesture == 1 and self.player_one.chosen_gesture == 4:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.player_two.chosen_gesture == 2 and self.player_one.chosen_gesture == 1:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.player_two.chosen_gesture == 2 and self.player_one.chosen_gesture == 3:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.player_two.chosen_gesture == 3 and self.player_one.chosen_gesture == 1:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.player_two.chosen_gesture == 3 and self.player_one.chosen_gesture == 4:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.player_two.chosen_gesture == 4 and self.player_one.chosen_gesture == 0:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.player_two.chosen_gesture == 4 and self.player_one.chosen_gesture == 2:
            self.player_two.score += 1
            print("player two wins this round!")
        elif self.computer.chosen_gesture == 0 and self.player_one.chosen_gesture == 2:
            self.computer.score += 1
            print("AI wins this round!")
        elif self.computer.chosen_gesture == 0 and self.player_one.chosen_gesture == 3:
            self.computer.score += 1
            print("AI wins this round!")
        elif self.computer.chosen_gesture == 1 and self.player_one.chosen_gesture == 0:
            self.computer.score += 1
            print("AI wins this round!")
        elif self.computer.chosen_gesture == 1 and self.player_one.chosen_gesture == 4:
            self.computer.score += 1
            print("AI wins this round!")
        elif self.computer.chosen_gesture == 2 and self.player_one.chosen_gesture == 1:
            self.computer.score += 1
            print("AI wins this round!")
        elif self.computer.chosen_gesture == 2 and self.player_one.chosen_gesture == 3:
            self.computer.score += 1
            print("AI wins this round!")
        elif self.computer.chosen_gesture == 3 and self.player_one.chosen_gesture == 1:
            self.computer.score += 1
            print("AI wins this round!")
        elif self.computer.chosen_gesture == 3 and self.player_one.chosen_gesture == 4:
            self.computer.score += 1
            print("AI wins this round!")
        elif self.computer.chosen_gesture == 4 and self.player_one.chosen_gesture == 0:
            self.computer.score += 1
            print("AI wins this round!")
        elif self.computer.chosen_gesture == 4 and self.player_one.chosen_gesture == 2:
            self.computer.score += 1
            print("AI wins this round!")
        else:
            self.player_one.score += 1
            print("Player one wins this round!")

    def player_one_turn(self):
        print("Player one's turn:")
        self.show_player_one_options()
        while True:
            try:
                self.player_one.chosen_gesture = int(input())
            except ValueError:
                    print("invalid")
                    continue
            else:
                return self.player_one.chosen_gesture

    def player_two_turn(self):
        print("Player two's turn:")
        self.show_player_two_options()
        while True:
            try:
                self.player_two.chosen_gesture = int(input())
            except ValueError:
                    print("invalid")
                    continue
            else:
                return self.player_two.chosen_gesture

    def computer_turn(self):
        print("Computers turn:")
        self.show_computers_options()
        self.computer.chosen_gesture = random.randint(0, 4)
        print(self.computer.chosen_gesture)

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

    def show_computers_options(self):
        gesture_index = 0
        for gesture in self.computer.gestures:
            print(f"press {gesture_index} for {gesture}")
            gesture_index += 1

    def display_winner(self):
        if self.computer.score > 1:
            print("AI wins best 2 out of 3!")
            quit()
        elif self.player_one.score > 1:
            print("player one wins best 2 out of 3!")
            quit()
        elif self.player_two.score > 1:
            print("player two wins best 2 out of 3!")
            quit()
