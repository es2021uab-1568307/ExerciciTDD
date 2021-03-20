# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:30:01 2021

@author: borja
"""

from main.game import *

def test_startOfGame():
    result = get_score()
    assert result == "love-All"