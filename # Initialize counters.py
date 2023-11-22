# Initialize counters
sentence_length = 0
word_count = 0
vowel_count = 0

# Input sentence ending with a period
input_sentence = input("Enter a sentence (end with a period): ")

# Iterate through each character in the sentence
for char in input_sentence:
    # Increase the sentence length counter
    sentence_length += 1
    
    # Check if the character is a letter and not a space
    if char.isalpha():
        # If the character is a vowel, increase the vowel count
        if char.lower() in 'aeiou':
            vowel_count += 1
    # Check if the character is a space
    elif char.isspace():
        # If it's a space, increase the word count
        word_count += 1

# The last character is a period, so don't count it in word count
word_count += 1

# Display the results
Write("Sentence length:", sentence_length)
Write("Word count:", word_count)
Write("Vowel count:", vowel_count)