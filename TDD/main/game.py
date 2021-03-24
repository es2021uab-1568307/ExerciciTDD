# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:32:15 2021

@author: borja
"""

class player:
    def __init__(self, name):
        self._name = name
        self._points = 0
    
    def wins_point(self, player) -> str:
        self._points += 1

class game:
    def get_score(player1, player2) -> str:
        if player1.points == 3:
            return "Deuce"
        if player1.points == 2 and player2.points == 2:
            return "Thirty-All"
        if player1.points == 1 and player2.points == 0:
            return "Fifteen-Love"
        if player1.points == 2:
            return "Thirty-Love"
        if player2.points == 1:
            return "Fifteen-All"
        return "Love-All"

    

