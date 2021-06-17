class Player_one:
    def __init__(self):
        self.name = ""
        self.chosen_gesture = [5]
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "Spock"]

    def choosen_gesture(self):
        print("override this method")
        pass
