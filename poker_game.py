#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:56:46 2019

@author: haleyporter
"""

#import random.choice
#cards = [2,3,4,5,6,7,8,9,10,J,Q,K,A]
#suits = [clubs, spades, hearts, diamonds]

#player_1 = [2,3,K,Q,7]
#player_2 = [8,10, ACE,J,2]

#player_1 = PokerGame()
#player_2 = PokerGame()
  
NUM_OF_PLAYERS = 2
 

class PokerGame:

    def __init__(self, players):
        self.players = players
        self.scores = []
        for i in range(PokerGame.NUM_OF_PLAYERS):
            self.scores.append(0)
 
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name
 
    def __lt__(self, other):
        return self.name < other.name
print(PokerGame)

class Suits:

    def __init__(self, color):
        print("instantiating the class")
        self.color = color  #this is a class attribute

    def describe(self):
        print("{} Car".format(self.color))

    def turn_left(self):
        print("Turning Left")

    def turn_right(self):
        print("Turning Right")

player_1 = Suits(color="clubs")
player_1.describe()
print(player_1.color)

player_1 = Suits(color="clubs")
player_1.describe()
print(player_1.color)


class PokerGame:
    def __init__(self, color, cards):
        self.color = color
        self.cards = cards
        self.speed = 0 # the car starts with the engine off

    def describe(self):
        print("Car with Model: {}. Color {}. Max Speed: {}".format(
            self.cards, self.color, self.max_speed))

    def describe_state(self):
        if self.speed == 0:
            print("The car is stopped")
        else:
            print("The car is driving at {} miles/hour".format(self.speed))

    def turn_left(self):
        print("Turning Left")

    def turn_right(self):
        print("Turning Right")

    def speed_up(self):
        # we can use pass when we define a method that we know we will use in the future
        # but we dont want to define it now
        pass

    def slow_down(self):
        pass

player_1 = PokerGame(
        cards="ACE",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="ACE",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="ACE",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="ACE",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="K",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="K",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="K",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="K",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="Q",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="Q",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="Q",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="Q",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="J",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="J",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="J",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="J",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="2",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="2",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="2",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="2",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="3",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="3",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="3",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="4",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="4",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="4",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="4",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="4",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="5",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="5",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="5",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="5",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="6",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="6",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="6",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="6",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="7",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="7",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="7",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="7",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="8",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="8",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="8",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="8",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="9",
        color="hearts", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="9",
        color="spades", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="9",
        color="diamonds", max_speed=140)
player_1.describe()
player_1.describe_state()

player_1 = PokerGame(
        cards="9",
        color="clubs", max_speed=140)
player_1.describe()
player_1.describe_state()



