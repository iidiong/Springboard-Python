 
def print_upper_words(words):
    """Uppercase each word from words list and print out on a separate line"""
    for word in words:
        print(word.upper())
       

def print_upper_words1(words):
    """Uppercase each word from words list that start with "e" or "E" and print out on a separate line"""
    for word in words:
        if(word.startswith("e") or word.startswith("E")):
            print(word.upper())
            
            
def print_upper_words2(words, must_start_with):
    """Uppercase each word from words list that start with a given set of letters and print out on a separate line"""
    for word in words:
        for letter in must_start_with:
            if(word.startswith(letter)):
                print(word.upper())

print_upper_words(["Hello", "hey", "goodbye", "yo", "yes"])
print("========")
print_upper_words1(["Hello", "hey", "goodbye", "yo", "yes","Edison", "Emmanuel"])
print("========")
print_upper_words2(["Hello", "hey", "goodbye", "yo", "yes",
                  "and"], must_start_with={"h", "H"})
