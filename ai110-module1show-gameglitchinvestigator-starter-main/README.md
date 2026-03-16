# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Game Purpose
The Game Glitch Investigator is a Streamlit-based number guessing game where players attempt to guess a randomly-generated secret number within a range determined by difficulty level. Players receive directional hints ("Go Higher" or "Go Lower") and earn/lose points based on their guesses. The game includes three difficulty levels (Easy: 1-20, Normal: 1-50, Hard: 1-100) with varying attempt limits.

### Bugs Found

1. **Reversed Hint Logic**: The directional hints were backwards. When a guess was too high, the game said "Go HIGHER!" when it should say "Go LOWER!" and vice versa.

2. **String Conversion Bug**: On even-numbered attempts, the secret was converted to a string, causing string comparisons instead of numeric comparisons. This led to incorrect hint logic due to lexicographic ordering (e.g., "2" > "100" evaluates to True).

3. **Hardcoded Range in "New Game"**: The "New Game" button used a hardcoded range of 1-100, ignoring the difficulty-specific ranges defined in `get_range_for_difficulty()`.

4. **Incomplete State Reset**: The "New Game" button didn't reset score, status, or history, and the game didn't reset properly when difficulty was changed mid-game.

5. **Attempts Counter Issue**: The attempts counter started at 1 instead of 0, causing off-by-one errors in attempt tracking.

### Fixes Applied

1. **Fixed Hint Messages**: Swapped the directional hint strings in `check_guess()` so "Too High" returns "Go LOWER!" and "Too Low" returns "Go HIGHER!"

2. **Removed String Conversion Bug**: Removed the conditional string conversion of the secret number on even attempts, ensuring all comparisons are numeric.

3. **Fixed "New Game" Range**: Updated the "New Game" button to call `get_range_for_difficulty(difficulty)` instead of hardcoding 1-100.

4. **Complete State Reset**: Modified the "New Game" button and difficulty change handler to reset all game state: attempts, score, status, history, and generate a new secret within the correct range.

5. **Corrected Attempts Initialization**: Changed initial attempts from 1 to 0 so the counter is accurate.

6. **Code Refactoring**: Moved all game logic functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) into `logic_utils.py` for separation of concerns.

7. **Comprehensive Testing**: Created 20 unit tests covering all game logic functions, including edge cases and the specific bug scenarios mentioned above. All tests pass.

## 📸 Demo

- [X] ![alt text](<Screenshot 2026-03-15 214054.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
