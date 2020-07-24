'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    length1 = len(word) # get the length of the string
    length2 = len("th") # get the length of "th" = 2

    # Base Case
    if (length1 == 0 or length1 < length2): # this will check the length of the string to see if it is 0, or less than 2
        return 0 # it has to be zero since the length of the word is less than 2

    # Recursive Case
    if (word[0 : length2] == "th"): # if you start the word at the 0 index, and go to the 2 index, see if the letters == "th"
        return count_th(word[length2 - 1:]) + 1 # if they do, up the count by + 1 and continue

    return count_th(word[length2 - 1:]) # if not return the final count