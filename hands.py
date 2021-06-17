
from player_one import Player_one
from player_two import Player_two
from computer import Computer

class Hands:
    def __init__(self):
        self.player_one = Player_one()
        self.player_two = Player_two()
        self.computer = Computer()

    def run_game(self):
        self.print_chosen_gestures()
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

    def single_player_mode(self):# computer mode
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one_turn()
            self.computer_turn()
            self.the_referee()
            self.display_winner()
            self.display_score()

    def two_player_mode(self):# human mode
        while self.player_one.score < 2 and self.computer.score < 2:
            self.player_one_turn()
            self.player_two_turn()
            self.the_referee()
            self.display_winner()

    def the_referee(self):
        if self.player_one.chosen_gesture[0] == self.player_two.chosen_gesture[0]:
            print("p1 and p2 tie")
        if self.player_one.chosen_gesture[0] == self.computer.chosen_gesture[0]:
            print("p1 and computer tie")
        elif self.player_one.chosen_gesture[0] == 0 and self.player_two.chosen_gesture[0] == 2 or 3:
            print("player one wins this round!")
        elif self.player_one.chosen_gesture[0] == 1 and self.player_two.chosen_gesture[0] == 0 or 4:
            print("player one wins this round!")
        elif self.player_one.chosen_gesture[0] == 2 and self.player_two.chosen_gesture[0] == 1 or 3:
            print("player one wins this round")
        elif self.player_one.chosen_gesture[0] == 3 and self.player_two.chosen_gesture[0] == 1 or 4:
            print("player one wins this round")
        elif self.player_one.chosen_gesture[0] == 4 and self.player_two.chosen_gesture[0] == 0 or 2:
            print("player one wins this round!")

        elif self.player_two.chosen_gesture[0] == 0 and self.player_one.chosen_gesture[0] == 2 or 3:
            print("player two wins this round!")
        elif self.player_two.chosen_gesture[0] == 1 and self.player_one.chosen_gesture[0] == 0 or 4:
            print("player two wins this round!")
        elif self.player_two.chosen_gesture[0] == 2 and self.player_one.chosen_gesture[0] == 1 or 3:
            print("player two wins this round")
        elif self.player_two.chosen_gesture[0] == 3 and self.player_one.chosen_gesture[0] == 1 or 4:
            print("player two wins this round")
        elif self.player_two.chosen_gesture[0] == 4 and self.player_one.chosen_gesture[0] == 0 or 2:
            print("player two wins this round!")

        elif self.computer.chosen_gesture[0] == 0 and self.player_one.chosen_gesture[0] == 2 or 3:
            print("AI wins this round!")
        elif self.computer.chosen_gesture[0] == 1 and self.player_one.chosen_gesture[0] == 0 or 4:
            print("AI wins this round!")
        elif self.computer.chosen_gesture[0] == 2 and self.player_one.chosen_gesture[0] == 1 or 3:
            print("AI wins this round")
        elif self.computer.chosen_gesture[0] == 3 and self.player_one.chosen_gesture[0] == 1 or 4:
            print("AI wins this round")
        elif self.computer.chosen_gesture[0] == 4 and self.player_one.chosen_gesture[0] == 0 or 2:
            print("AI wins this round!")

    def print_chosen_gestures(self):
        print(self.player_one.chosen_gesture[0])
        print(self.player_two.chosen_gesture[0])
        print(self.computer.chosen_gesture[0])

    def player_one_turn(self):
        print("Player one's turn:")
        self.show_player_one_options()
        chosen_input = int(input())
        self.player_one.chosen_gesture.insert(0, chosen_input)

    def player_two_turn(self):
        print("Player two's turn:")
        self.show_player_two_options()
        chosen_input = int(input())
        self.player_two.chosen_gesture.insert(0, chosen_input)

    def computer_turn(self):
        print("Computers turn:")
        self.show_computers_options()
        self.computer.chosen_gesture.insert(0, self.computer.random_gesture_generator())

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

    def test_score(self): # for testing scoring.
        self.player_one.score += 1

    def display_winner(self):
        if self.computer.score == 2:
            print("AI wins!")
        if self.player_one.score == 2:
            print("player one wins!")
        if self.player_two.score == 2:
            print("player two wins!")

    def display_score(self):
        print("player one's score is "f"{self.player_one.score}")
        print("player two's score is "f"{self.player_two.score}")

