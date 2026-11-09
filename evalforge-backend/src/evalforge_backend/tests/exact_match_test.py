#!/usr/bin/env python3
"""
 Enter module docstring here
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------


# ---------- Third Party Imports ----------


# ---------- Project Level Imports ----------
from evalforge_backend.verifiers.exact_match import verify_exact_match

# ---------- Begin File ----------


def test_identical_strings_return_true():
    identical_strings = verify_exact_match("Is this the same string?", "Is this the same string?")
    
    assert identical_strings == True

def test_non_identical_strings_return_false():
    non_identical_strings = verify_exact_match("Is this the same string?", "Is this the same string? ")
    
    assert non_identical_strings == False

def test_case_differences_return_false():
    non_identical_strings = verify_exact_match("is this the same string?", "IS THIS THE SAME STRING?")
    
    assert non_identical_strings == False

def test_case_leading_and_trailing_white_space_return_false():
    leading_whitespace = verify_exact_match(" is this the same string?", "is this the same string?")
    trailing_whitespace = verify_exact_match("is this the same string? ", "is this the same string?")
    
    assert leading_whitespace == False
    assert trailing_whitespace == False

def test_case_empty_string_return_true():
    empty_strings = verify_exact_match("", "")
    
    assert empty_strings == True
    
def test_case_empty_candidate_populated_expected_return_false():
    empty_candidate_populated_expected = verify_exact_match("", "This is a test")
    
    assert empty_candidate_populated_expected == False

def test_case_multiple_calls_return_same_result_return_true():
    call_1 = verify_exact_match("true", "true")
    call_2 = verify_exact_match("true", "true")
    call_3 = verify_exact_match("true", "true")
    call_4 = verify_exact_match("true", "true")
    call_5 = verify_exact_match("true", "true")
    
    assert call_1 == True
    assert call_2 == True
    assert call_3 == True
    assert call_4 == True
    assert call_5 == True
