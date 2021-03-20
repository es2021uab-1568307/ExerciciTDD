# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:30:01 2021

@author: borja
"""
import pytest

from main.game import game

@pytest.fiture()
def setup() -> game:
    return game("Toni", "Carla")
@pytest.fixture()
def teardown():
    return

"""@pytest.mark.parametrize("score_player_1, score_player_2, expected_result", [
    (0, 0, "love-all")
    ]
    ),
"""
def test_startOfGame(setup):
    game = setup
    result = game.get_score()
    assert result == "love-All"
    
def test_fifteenAll_afterPlayer1Scores(setup):
    game = setup
    
    game.wins_point("Toni")
    result = game.get_score()
    assert result == "fifteen-all"
    
def test_Player1AndPlayer2onePoint_fifteenAll(setup):
    game = setup
    
    game.wins_point("Toni")
    game.wins_point("Carla")
    result = game.get_score()
    
    assert result == "Fifteen-all"
    
def test_Player1TwoPointsAndPlayer2onePoint(setup):
    game = setup
    
    game.wins_point("Toni")
    game.wins_point("Carla")
    result = game.get_score()
    
    assert result == "thirty-fifteen"