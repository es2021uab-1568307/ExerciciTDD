# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:32:15 2021

@author: borja
"""

    

class game:
    
    def __init__(self, player1:str, player2: str):
        self._player1 = player1
        self._player2 = player2
        self._wins = ""
        
    def wins_point(self, player: str):
        self._wins = player
        
    def get_score(self) -> str:
        if self._wins == self.player1:
            return "Fifteen-love"
        if self._wins == self.player2:
            return "Fifteen-love"
        return "love-All"