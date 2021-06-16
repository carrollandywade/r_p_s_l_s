from player_one import Player_one
from player_two import Player_two
from computer import Computer


class Hands:
    def __init__(self):
        self.player_one = Player_one
        self.player_two = Player_two
        self.choose_one_or_two_player_mode()
        self.game_rounds()

    def run_game(self):
        self.display_welcome()
        self.display_instructions()

    def display_welcome(self):
        print("Welcome to Rocks, Paper, Scissors, Lizards, Spock!")

    def display_instructions(self):
        print("instructions.")

    def choose_one_or_two_player_mode(self):
        print("1p or 2p")
        if: response == 2
        self.player_two = Player_two()
        else:
        self.player_two = Computer()
        pass



    def game_rounds(self):
        print("Player one: Choose: rpsls")
        self.show_rpsls_options()
        chosen_gesture = (input())
        print("Player two: Choose: rpsls")
        self.show_rpsls_options()
        chosen_gesture = (input())




            #player one choose gesture
            #player two choose gesture
            #determine winner of round, winner score increases
            #loop to continure untill best of 3 occurs


    def show_rpsls_options(self):


        #end game
            #display winner

