# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:32:15 2021

@author: 432-5
"""

class player:
    def __init__(self, name):
        self._name = name
        self._points = 0
    
    def wins_point(self, player) -> str:
        self._points += 1
        
class game:    
    def get_score(player1, player2) -> str:

        """------PUNTS WIN PLAYER 1-----------"""
        if player1.points > player2.points:
            if player2.points == 0:
                if player1.points == 1:
                    return "Fifteen-Love"
                if player1.points == 2:
                    return "Thirty-Love"
                if player1.points == 3:
                    return "Forty-Love"

            if player2.points == 1:
                if player1.points == 2:
                    return "Thirty-Fifteen"
                if player1.points == 3:
                    return "Forty-Fifteen"

            if player2.points == 2:
                if player1.points == 3:
                    return "Forty-Thirty"

            if player2.points >= 3:
                if player1.points - player2.points == 1:
                    return "Advantage player1"
            return "Win for player1"

        """------PUNTS WIN PLAYER 2-----------"""
        if player1.points < player2.points:
            if player1.points == 0:
                if player2.points == 1:
                    return "Love-Fifteen"
                if player2.points == 2:
                    return "Love-Thirty"
                if player2.points == 3:
                    return "Love-Forty"

            if player1.points == 1:
                if player2.points == 2:
                    return "Fifteen-Thirty"
                if player2.points == 3:
                    return "Fifteen-Forty"

            if player1.points == 2:
                if player2.points == 3:
                    return "Thirty-Forty"

            if player1.points >= 3:
                if player2.points - player1.points == 1:
                    return "Advantage player2"
            return "Win for player2"

            """------PUNTS EMPATATS-----------"""
        if player1.points == 2:
            return "Thirty-All"
        if player1.points == 1:
            return "Fifteen-All"
        if player1.points == 0:
            return "Love-All"
        return "Deuce"
    
