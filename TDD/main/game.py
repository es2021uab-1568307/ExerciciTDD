# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:32:15 2021

@author: borja
"""

class player:
    def __init__(self, name):
        self._name = name
        self._points = 0
    
    def wins_point(self, player: str):
        self._points += 1
        
    def get_score(player1, player2) -> str:
        if player1._points == 1 and player2._points == 0:
            return "fifteen-love"
        if player1._points == 2:
            return "thirty-love"
        if player2._points == 1:
            return "fifteen-all"
        return "love-all"

    

