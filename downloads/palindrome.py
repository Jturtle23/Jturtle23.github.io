# palindrome.py

import sys

while True:
    print('Check if a word or number is a palindrome.\nType "list" to list some palindromes.\nType "exit" to exit the program.\n')
    text = input('- ')
    
    if text.lower() == 'exit':
        sys.exit()
        
    elif text.lower() == 'list':
        print('\nHere are some palindromes:')
        print('\n  1. Taco cat\n  2. Do geese see God?\n  3. As I pee, sir, I see Pisa!\n  4. Mr. Owl ate my metal worm!\n  5. Stressed desserts\n')
        
    else:
        def palindrome(text):
        
            new_text = ''    
            for char in text.lower():
                if char.isalnum():
                    new_text += char
                elif char == ' ':
                    char = ''
                    new_text += char
            if new_text == '':
                return 'error' # So that all non-alphanumeric strings ("-?><-", "-=-", etc) will not be allowed
            
           
            # Create new empty string "text_to_check"
            # Make text_to_check palindromic and compare it with new_text
            text_to_check = ''
            current_letter_index = -1
            for char in new_text:
                text_to_check += new_text[current_letter_index]
                current_letter_index -= 1
            if text_to_check == new_text:
                return True
            else:
                return False
    
        text_is_palindrome = palindrome(text)
        if text_is_palindrome == 'error':
            print(f'Error: Please do not enter non-alphanumeric strings.\n')
        elif text_is_palindrome:
            print(f'"{text}" is a palindrome.\n')
        elif not text_is_palindrome:
            print(f'"{text}" is not a palindrome.\n')