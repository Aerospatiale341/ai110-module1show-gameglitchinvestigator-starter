# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

--- When I initially loaded the game it appeared decently well-made (prior to any actually testing), however this illusion was quickly dispelled once actually trying to run the game. First, the hint logic is flawed (expected the reverse) as when the secret was 98 the hints were "Go Lower" for (50, 25, 13, 7, 3, 1, 97) and "Go Higher" for (99). I then noticed the "New Game" button was inoperable once the 'Game Over' state was reached, which prevented me from resetting the game state as expected. When I went to "Easy" and "Hard" mode, I noticed the secret number generation range is independent of difficulty level, always in range 1 - 100 rather than the applicable difficulty secret number range.

--- In subsequent runs, I identified the following bugs/design flaws: 
      -When the webpage is refreshed or initially it counts towards the attempt count 
      -The banner below "Make a Guess" appears to reflect the true range of secret number generation
      -Nonsensical assignment of secret number range and number of attempts with regards to difficulty level
      -Similar to the 'Game Over' state bug above, the 'Win' state is reached the "Submit Guess" button remains inoperable following new game creation
      -Even attempt's not registered sometimes, when network traffic analyzed it is sending, the program is not recognizing it (requires further investigation as time allows)
        Guess history incorrectly updates when input not registered
      -Score not reset when new game started
      -When difficulty is switched mid-game, new game instance not forced (secret number and number attempts used persist between difficulty swaps) 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---I used Copilot for this project as I have used Gemini in previous projects and Claude for all in class purposes. Copilot correctly identified the issue I noted with the reversal of the hint logic, I verified this both using test cases and manually. Copilot did correctly fix the secret number ranges, but did not correct the banner logic at the same time. I caught this during manual testing immediately and fixed it.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---I used pytest to test the logic for functionality, but manually tested to ensure that the displayed information was also as intended. Both Copilot and I did not update the secret number range portion of the banner, I caught this during manual testing when I switched between difficulties. This showed me that this banner was hard coded.  I used Copilot to design and write the tests and verified that they made sense.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

--- The secret number kept changing because Streamlit reruns the entire script from top to bottom every time the user interacts with the app (button clicks, text input, etc.). Without proper session state management, `random.randint()` was being called on every rerun, generating a new secret number. Streamlit's session state is like a "memory", it's a dictionary attached to each user session that remembers values between interactions. To a friend, I'd explain, "When you click a button, it reruns the entire code. Session state is how the app remembers things from the previous run so they don't reset." The fix was checking `if "secret" not in st.session_state:` before generating a new secret, ensuring it's only created once and then stored in session state.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--- I want to reuse the combination of automated testing (pytest) with manual testing—the pytest tests verified the logic was correct, but manual testing revealed UI/display issues that automated tests couldn't catch. This dual approach caught bugs like the hardcoded banner range that pure logic tests would have missed. Next time I work with AI, I would be more specific in asking about edge cases and state management upfront, rather than discovering issues through testing. This project taught me that AI-generated code is a starting point that requires thorough testing and careful code review. It can have logical flaws or overlook critical details like state management, even when the core logic appears sound.
