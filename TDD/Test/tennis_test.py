# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:30:01 2021

@author: borja
"""
import pytest

from main.game import *

@pytest.fixture()
def setup():
    player1=player("Toni")
    player2=player("Carla")
    return player1, player2
@pytest.fixture()
def setup2() -> player:
    return player("Carla")
@pytest.fixture()
def teardown():
    return

@pytest.mark.parametrize("score_player_1, score_player_2, expected_result", [
    (0, 0, "love-all"),
    (1,0, "fifteen-love"),
    (2,0, "thirty-love"),
    (1,1, "fifteen-all")]
    )
def test_Game(setup, score_player_1, score_player_2, expected_result):
    player1=setup[0]
    player2=setup[1]

    player1._points=score_player_1
    player2._points=score_player_2
    result = game.get_score(player1,player2)
    assert result == expected_result
    
