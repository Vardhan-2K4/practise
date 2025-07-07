import string

def get_unique_words(sentence):
    """
    Processes a sentence to extract unique words, ignoring case and punctuation,
    and returns them in alphabetical order.

    Args:
        sentence (str): The input sentence from the user.

    Returns:
        list: A sorted list of unique words. Returns an empty list if no words are found.
    """
    if not sentence:
        return []

    # 1. Convert to lowercase
    sentence = sentence.lower()

    # 2. Remove punctuation
    # Create a translation table to replace punctuation with spaces
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    cleaned_sentence = sentence.translate(translator)

    # 3. Split the sentence into words
    # Filter out empty strings that might result from multiple spaces or punctuation at ends
    words = [word for word in cleaned_sentence.split() if word]

    # 4. Use a set to store unique words
    unique_words_set = set(words)

    # 5. Convert the set to a list and sort alphabetically
    unique_words_list = sorted(list(unique_words_set))

    return unique_words_list

def unique_word_lister_program():
    """
    Main function to run the unique word lister program.
    Prompts the user for a sentence and displays unique words.
    """
    print("Welcome to the Unique Word Lister!")
    print("Enter a sentence to see its unique words in alphabetical order.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nEnter a sentence: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting Unique Word Lister. Goodbye!")
            break
        elif not user_input:
            print("Input cannot be empty. Please enter a sentence or 'exit'.")
            continue

        unique_words = get_unique_words(user_input)

        if unique_words:
            print("\n--- Unique Words (Alphabetical Order) ---")
            for word in unique_words:
                print(word)
            print("-----------------------------------------")
        else:
            print("No words found in the input sentence after processing.")

if __name__ == "__main__":
    unique_word_lister_program()