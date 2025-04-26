# Quizzler - A Trivia Game

## Overview

Quizzler is a fun and interactive trivia game built using Python's Tkinter library for the graphical user interface. The game fetches trivia questions from an open-source API, presents them to the user, and allows them to answer True or False. It keeps track of the user's score and provides feedback on their answers.

## Features

* **Engaging GUI:** A clean and user-friendly graphical interface built with Tkinter.
* **Trivia Questions:** Fetches trivia questions with True/False answers from the Open Trivia Database API.
* **Question Display:** Presents one question at a time to the user.
* **True/False Answers:** Users can answer each question by clicking the True or False buttons.
* **Score Tracking:** Keeps a real-time score of correct answers.
* **Answer Feedback:** Provides visual feedback (green for correct, red for incorrect) after each answer.
* **Game End:** Detects the end of the question set and displays a "You've reached the end!" message.

## How to Run

1.  **Prerequisites:** Ensure you have Python 3 installed on your system. You also need to install the `requests` and `pandas` libraries if you haven't already. You can install them using pip:

    ```bash
    pip install requests pandas
    ```

2.  **Download Images:** Download the `true.png` and `false.png` images and place them in a directory named `images` within the same directory as your Python scripts.

3.  **Run `main.py`:** Navigate to the directory containing the Python files in your terminal and execute the `main.py` script:

    ```bash
    python main.py
    ```

    This will launch the Quizzler game window.

## Project Structure

The project consists of the following Python files:

* `data.py`: Fetches trivia question data from the Open Trivia Database API and stores it in the `question_data` list.
* `main.py`: Initializes the game by creating `Question` objects from the `question_data`, instantiating the `QuizBrain` to manage the game logic, and launching the `QuizInterface` for the user interaction.
* `question_model.py`: Defines the `Question` class, which represents a single trivia question with its text and correct answer.
* `quiz_brain.py`: Contains the `QuizBrain` class, responsible for managing the game flow, keeping track of the question number and score, fetching the next question, and checking the user's answers.
* `ui.py`: Implements the `QuizInterface` class, which creates the graphical user interface using Tkinter, displays questions, handles user input (True/False button clicks), shows feedback, and updates the score.

Additionally, there is an `images` directory containing:

* `true.png`: Image for the "True" button.
* `false.png`: Image for the "False" button.

## Code Overview

* **`data.py`**:
    * Uses the `requests` library to make a GET request to the Open Trivia Database API.
    * Retrieves 10 boolean (True/False) trivia questions.
    * Parses the JSON response and stores the question data in the `question_data` list.

* **`main.py`**:
    * Imports the necessary classes (`Question`, `QuizBrain`, `QuizInterface`) and the `question_data`.
    * Iterates through the `question_data` to create `Question` objects and populates the `question_bank` list.
    * Creates an instance of `QuizBrain` with the `question_bank`.
    * Creates an instance of `QuizInterface`, passing the `QuizBrain` object to manage the UI and game logic.

* **`question_model.py`**:
    * Defines a simple `Question` class with an `__init__` method to initialize the question's text (`self.text`) and its correct answer (`self.answer`).

* **`quiz_brain.py`**:
    * The `QuizBrain` class manages the game state.
    * `__init__(self, q_list)`: Initializes the question number to 0, the score to 0, and stores the list of `Question` objects.
    * `still_has_questions(self)`: Returns `True` if there are more questions remaining, `False` otherwise.
    * `next_question(self)`: Retrieves the next question from the `question_list`, increments the `question_number`, and returns the question text after unescaping any HTML entities.
    * `check_answer(self, user_answer)`: Checks if the `user_answer` matches the `correct_answer` of the current question, updates the score if correct, and returns `True` if the answer is right, `False` otherwise.

* **`ui.py`**:
    * The `QuizInterface` class handles the graphical user interface.
    * `__init__(self, quiz_brain: QuizBrain)`: Initializes the main window, sets the title and background color, creates labels for the score and question text, creates True and False buttons with corresponding images, and calls `get_next_question()` to start the game.
    * `get_next_question(self)`: Updates the question text on the canvas, updates the score label, and disables the buttons when all questions have been answered.
    * `true_pressed(self)`: Called when the True button is clicked; checks the answer and triggers feedback.
    * `false_pressed(self)`: Called when the False button is clicked; checks the answer and triggers feedback.
    * `give_feedback(self, is_right)`: Changes the canvas background color to green for a correct answer and red for an incorrect answer, then calls `get_next_question()` after a 1-second delay to move to the next question.

## Potential Enhancements

* Implement different difficulty levels or categories of questions.
* Add a visual progress bar or question counter.
* Display the final score at the end of the quiz.
* Allow users to play again.
* Improve the visual design and styling of the GUI.
