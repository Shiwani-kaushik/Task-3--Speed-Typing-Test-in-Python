import time


def run_speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)
    input("Press Enter when you are ready.")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    characters_typed = len(user_input)
    typing_speed = words_typed / elapsed_time * 60

    print("\n--- Results ---")
    print("Time taken:", round(elapsed_time, 2), "seconds")
    print("Words typed:", words_typed)
    print("Characters typed:", characters_typed)
    print("Typing speed:", round(typing_speed, 2), "words per minute")


run_speed_typing_test()

