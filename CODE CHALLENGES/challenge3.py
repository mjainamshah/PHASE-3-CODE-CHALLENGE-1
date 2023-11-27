def consonant(s):
    # Function to calculate the value of a substring based on the consonant values
    def substring_value(sub):
        # Assigns values to consonants using their position/index in the alphabet
        consonant_values = {c: ord(c) - ord('a') + 1 for c in 'abcdefghijklmnopqrstvwxyz'}
        # Calculates the value of the substring by summing up the values of its characters
        return sum(consonant_values[char] for char in sub)
    
    # Removes the vowels from the string
    consonant_substrings = ''.join(c if c not in 'aeiou' else ' ' for c in s)
    # Splits the string into consonant substrings
    consonant_substrings = consonant_substrings.split()
    
    # Calculates the values of consonant substrings & finds the maximum
    max_value = max(substring_value(sub) for sub in consonant_substrings)
    
    return max_value

# TESTS FOR CONFIRMATION:
print(consonant("zodiacs"))   
print(consonant("strength"))
