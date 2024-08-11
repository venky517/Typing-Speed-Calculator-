# Typing-Speed-Calculator-
# Typing Speed and Accuracy Test

This Python script allows users to test their typing speed and accuracy. It provides feedback based on the speed (in Words Per Minute) and accuracy of the typed text compared to a predefined sentence.

## Features

- **Typing Speed Measurement:** Calculates the typing speed in Words Per Minute (WPM).
- **Accuracy Calculation:** Computes the accuracy percentage based on the correctness of typed words.
- **Feedback:** Provides feedback on typing speed and accuracy.

## Prerequisites

- Python 3.x installed on your system.

## How to Use

1. **Download or Clone the Repository:**
   - Download the script file or clone the repository to your local machine.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using the following command:
     ```bash
     python typing_test.py
     ```

3. **Follow the Instructions:**
   - The script will display a sentence that you need to type as quickly and accurately as possible.
   - Press Enter to start typing.
   - After you finish typing, press Enter again to submit your text.

4. **View Results:**
   - The script will display your typing speed (in WPM) and accuracy (as a percentage).
   - It will also provide feedback based on your typing speed.

## Code Explanation

- **`calculate_wpm(start_time, end_time, typed_text)`**
  - Calculates the typing speed in Words Per Minute based on the start and end times and the typed text.

- **`calculate_accuracy(original_text, typed_text)`**
  - Computes the accuracy by comparing the typed text with the original text.

- **`main()`**
  - The main function that drives the script. It displays the sentence, records typing time, and calculates both speed and accuracy.

## Example

Here's an example of how the output might look:

