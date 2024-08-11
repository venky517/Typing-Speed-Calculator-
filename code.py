import time

def calculate_wpm(start_time, end_time, typed_text):
    total_time = end_time - start_time
    word_count = len(typed_text.split())
    wpm = (word_count / total_time) * 60
    return wpm

def calculate_accuracy(original_text, typed_text):
    original_words = original_text.split()
    typed_words = typed_text.split()
    
    correct_words = 0
    for original_word, typed_word in zip(original_words, typed_words):
        if original_word == typed_word:
            correct_words += 1
            
    accuracy = (correct_words / len(original_words)) * 100
    return accuracy

def main():
    # Predefined sentence
    sentence = "The quick brown fox jumps over the lazy dog."
    
    print("Type the following sentence as fast and accurately as you can:")
    print(sentence)
    
    input("Press Enter to start...")
    
    start_time = time.time()
    typed_text = input("\nStart typing here: ")
    end_time = time.time()
    
    wpm = calculate_wpm(start_time, end_time, typed_text)
    accuracy = calculate_accuracy(sentence, typed_text)
    
    print(f"\nYour typing speed is: {wpm:.2f} WPM")
    print(f"Your typing accuracy is: {accuracy:.2f}%")
    
    if wpm > 40:
        print("Great job! You have a good typing speed.")
    elif wpm > 20:
        print("Good effort! With some practice, you can improve your speed.")
    else:
        print("Keep practicing to improve your typing speed.")

if __name__ == "__main__":
    main()