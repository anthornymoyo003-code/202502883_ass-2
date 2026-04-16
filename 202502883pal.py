# 202510814_palindrome.py
# Data Structures I Assignment
# Palindrome Checker using Array of Characters

def is_palindrome(word):
    # Convert word into list of characters (array)
    char_array = list(word)

    # Reverse the array
    reversed_array = char_array[::-1]

    # Compare original and reversed
    if char_array == reversed_array:
        return True
    else:
        return False


def main():
    while True:
        print("\n===== PALINDROME CHECKER =====")
        print("1. Check Word")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            word = input("Enter a word: ")

            if is_palindrome(word):
                print(f'"{word}" is a palindrome.')
            else:
                print(f'"{word}" is NOT a palindrome.')

        elif choice == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
