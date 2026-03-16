from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score
# These tests cover the corrected game logic functions in logic_utils.py.
# These tests were generated using Copilot agent mode, which is designed to create comprehensive unit tests for the game logic functions. 
# The tests cover various scenarios for each function, including edge cases and typical use cases, to ensure that the game behaves as expected under different conditions.
#Run this using the command: python -m pytest tests/test_game_logic.py -v

# ===== check_guess() tests =====

def test_winning_guess():
    """If the secret is 50 and guess is 50, it should be a win"""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "🎉" in message

def test_guess_too_high():
    """If secret is 50 and guess is 60, hint should be 'Too High' with 'Go LOWER!' message"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "Go LOWER!" in message

def test_guess_too_low():
    """If secret is 50 and guess is 40, hint should be 'Too Low' with 'Go HIGHER!' message"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "Go HIGHER!" in message

def test_check_guess_with_multiple_values():
    """Test various guess scenarios to confirm hint logic is correct"""
    # Secret is 98
    secret = 98
    assert check_guess(50, secret)[0] == "Too Low"  # 50 < 98
    assert check_guess(25, secret)[0] == "Too Low"  # 25 < 98
    assert check_guess(99, secret)[0] == "Too High"  # 99 > 98
    assert check_guess(98, secret)[0] == "Win"  # 98 == 98

def test_check_guess_hint_messages_are_correct():
    """Verify hint messages match the outcome"""
    # Too High should say "Go LOWER!"
    outcome, message = check_guess(100, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    # Too Low should say "Go HIGHER!"
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# ===== parse_guess() tests =====

def test_parse_guess_valid_integer():
    """Valid integer input should parse correctly"""
    ok, guess_int, error = parse_guess("50")
    assert ok is True
    assert guess_int == 50
    assert error is None

def test_parse_guess_decimal_input():
    """Decimal input like '50.7' should be converted to integer"""
    ok, guess_int, error = parse_guess("50.7")
    assert ok is True
    assert guess_int == 50
    assert error is None

def test_parse_guess_empty_string():
    """Empty string should return error"""
    ok, guess_int, error = parse_guess("")
    assert ok is False
    assert guess_int is None
    assert error == "Enter a guess."

def test_parse_guess_none_input():
    """None input should return error"""
    ok, guess_int, error = parse_guess(None)
    assert ok is False
    assert guess_int is None
    assert error == "Enter a guess."

def test_parse_guess_invalid_input():
    """Non-numeric input should return error"""
    ok, guess_int, error = parse_guess("abc")
    assert ok is False
    assert guess_int is None
    assert error == "That is not a number."

def test_parse_guess_special_characters():
    """Special characters should return error"""
    ok, guess_int, error = parse_guess("@#$")
    assert ok is False
    assert error == "That is not a number."

# ===== get_range_for_difficulty() tests =====

def test_easy_difficulty_range():
    """Easy difficulty should return range 1-20"""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_difficulty_range():
    """Normal difficulty should return range 1-50"""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_hard_difficulty_range():
    """Hard difficulty should return range 1-100"""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_invalid_difficulty_defaults_to_normal():
    """Invalid difficulty should default to Normal range (1-100)"""
    low, high = get_range_for_difficulty("InvalidDifficulty")
    assert low == 1
    assert high == 100

# ===== update_score() tests =====

def test_update_score_on_win():
    """Winning should award points based on attempt number"""
    # Attempt 1: 100 - 10 * (1 + 1) = 80 points
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

    # Attempt 5: 100 - 10 * (5 + 1) = 40 points
    new_score = update_score(0, "Win", 5)
    assert new_score == 40

def test_update_score_minimum_points():
    """Winning after many attempts should have minimum of 10 points"""
    # Attempt 10: 100 - 10 * (10 + 1) = -10, capped at 10
    new_score = update_score(0, "Win", 10)
    assert new_score == 10

def test_update_score_on_too_high():
    """Too High guess should deduct 5 points"""
    new_score = update_score(100, "Too High", 1)
    assert new_score == 95

def test_update_score_on_too_low():
    """Too Low guess should deduct 5 points"""
    new_score = update_score(100, "Too Low", 1)
    assert new_score == 95

def test_update_score_accumulates():
    """Score should accumulate through multiple guesses"""
    score = 0
    score = update_score(score, "Too Low", 1)  # -5
    assert score == -5
    score = update_score(score, "Too High", 2)  # -5
    assert score == -10
    score = update_score(score, "Win", 3)  # +(100 - 10*4) = +60
    assert score == 50
