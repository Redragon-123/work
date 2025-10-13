# Frequency analysis is a method of breaking certain ciphers which involves counting the frequency of letters/symbols
# because English has quite a clear distribution of letters, with spikes on common letters such as 'e', 'i' and 's'

# Ask the user for a filename
# open and read the file 
# and count how many instances of each letter are in the program
# hint: use a dictionary!

# Additional hints:
# - Remember to handle the case where the file might not exist
# - You'll need to check each character to see if it's a letter
# - Dictionary pattern: if key exists, increment; if not, set to 1
# - Consider converting to lowercase for consistent counting
filename = input("Enter the filename: ")
letter_count = {}
try:
    with open(filename, 'r') as infile:
        for char in filename:
            if char.isalpha():
                lower_char = char.lower()
                if lower_char in letter_count:
                    letter_count[lower_char] += 1
                else:
                    letter_count[lower_char] = 1
    for letter, count in sorted(letter_count.items()):
        print(f"{letter}: {count}")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
