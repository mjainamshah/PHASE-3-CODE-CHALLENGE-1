def exactly_two_positive(a, b, c):
    positive_count = 0         # Counts the number of positive numbers among the given integers
    
    if a > 0:                  # Checks each number if it's positive (greater than zero) & increments positive_count by 1
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2 # Returns True if exactly two out of three integers are positive, otherwise returns a False


# TESTS FOR CONFIRMATIONS:
# print(exactly_two_positive(2, 4, -3))    
# print(exactly_two_positive(-4, 6, 8))   
# print(exactly_two_positive(4, -6, 9))   
# print(exactly_two_positive(-4, 6, 0))   
# print(exactly_two_positive(4, 6, 10))   
# print(exactly_two_positive(-14, -3, -4))
