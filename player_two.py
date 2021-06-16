class Player_two:
    def __init__(self):
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "Spock"]

    def choose_gesture(self):
        print("override this method")
        pass