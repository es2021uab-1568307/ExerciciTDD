# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:30:01 2021

@author: borja
"""
import pytest

from main.game import *

@pytest.fixture()
def setup() -> player:
    player1=player("Toni")
    player2=player("Carla")
    return player1, player2

@pytest.fixture()
def teardown():
    return

@pytest.mark.parametrize("score_player_1,score_player_2,expected_result", [
    (0, 0, "Love-All"),
    (1, 0, "Fifteen-Love"),
    (2, 0, "Thirty-Love"),
    (1, 1, "Fifteen-All"),
    (2, 2, "Thirty-All"),
    (3, 3, "Deuce"),
    (4, 4, "Deuce"),
    (0, 1, "Love-Fifteen"),
    (0, 2, "Love-Thirty"),
    (3, 0, "Forty-Love"),
    (0, 3, "Love-Forty"),
    (4, 0, "Win for player1"),
    (0, 4, "Win for player2"),
    (2, 1, "Thirty-Fifteen"),
    (1, 2, "Fifteen-Thirty"),
    (3, 1, "Forty-Fifteen"),
    (1, 3, "Fifteen-Forty"),
    (4, 1, "Win for player1"),
    (1, 4, "Win for player2"),
    (3, 2, "Forty-Thirty"),
    (2, 3, "Thirty-Forty"),
    (4, 2, "Win for player1"),
    (2, 4, "Win for player2")
])


def test_startOfGame(setup,score_player_1, score_player_2, expected_result):
    player1 = setup[0]
    player2 = setup[1]
    player1.points = score_player_1
    player2.points = score_player_2
    result = game.get_score(player1, player2)
    assert result == expected_result


"""
    (0, 0, "Love-All") +
    (1, 1, "Fifteen-All") +
    (1, 0, "Fifteen-Love") +
    (2, 0, "Thirty-Love") +
    (2, 2, "Thirty-All") +
    (3, 3, "Deuce") +
    (4, 4, "Deuce") +
    (0, 1, "Love-Fifteen") +
    (0, 2, "Love-Thirty") +
    (3, 0, "Forty-Love") +
    (0, 3, "Love-Forty") +
    (4, 0, "Win for player1") +
    (0, 4, "Win for player2") +
    (2, 1, "Thirty-Fifteen") +
    (1, 2, "Fifteen-Thirty") +
    (3, 1, "Forty-Fifteen") +
    (1, 3, "Fifteen-Forty") +
    (4, 1, "Win for player1") +
    (1, 4, "Win for player2") +
    (3, 2, "Forty-Thirty") + 
    (2, 3, "Thirty-Forty") +
    (4, 2, "Win for player1") +
    (2, 4, "Win for player2") +
    (4, 3, "Advantage player1")
    (3, 4, "Advantage player2")
    (5, 4, "Advantage player1")
    (4, 5, "Advantage player2")
    (15, 14, "Advantage player1")
    (14, 15, "Advantage player2")
    (6, 4, "Win for player1")
    (4, 6, "Win for player2")
    (16, 14, "Win for player1")
    (14, 16, "Win for player2")
"""
