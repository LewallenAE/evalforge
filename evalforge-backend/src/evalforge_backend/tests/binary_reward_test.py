#!/usr/bin/env python3
"""
 Enter module docstring here
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------


# ---------- Third Party Imports ----------


# ---------- Project Level Imports ----------
from evalforge_backend.rewards.binary_reward import calculate_binary_reward

# ---------- Begin File ----------


def test_binary_reward_true():
    reward = calculate_binary_reward(True)
    assert reward == 1.0
    
def test_binary_reward_false():
    reward = calculate_binary_reward(False)
    assert reward == 0.0
    
def test_binary_repeated_calls_reward_true():
    reward_1 = calculate_binary_reward(True)
    reward_2 = calculate_binary_reward(True)
    reward_3 = calculate_binary_reward(True)
    reward_4 = calculate_binary_reward(True)

    assert reward_1 == 1.0
    assert reward_2 == 1.0
    assert reward_3 == 1.0
    assert reward_4 == 1.0

def test_binary_repeated_calls_reward_false():
    reward_1 = calculate_binary_reward(False)
    reward_2 = calculate_binary_reward(False)
    reward_3 = calculate_binary_reward(False)
    reward_4 = calculate_binary_reward(False)
    
    assert reward_1 == 0.0
    assert reward_2 == 0.0
    assert reward_3 == 0.0
    assert reward_4 == 0.0
    
def test_binary_is_instance_float():
    reward = calculate_binary_reward(True)
    
    assert isinstance(reward, float)
    
