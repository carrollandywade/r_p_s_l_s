from player_two import Player_two
import random


class Computer(Player_two):
    def __init__(self):
        self.random_gesture = []
        super().__init__()


def random_gesture_generator(self):
    print(random.randint(0, 4))


