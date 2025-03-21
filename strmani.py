def longest_word(sentence):
    words = sentence.split()  
    longest = ""  
    
    for word in words:
        clean_word = "".join(filter(str.isalnum, word))  
        if len(clean_word) > len(longest):
            longest = clean_word
    
    return longest

sentence = input("Enter a sentence: ")
print("Longest word:", longest_word(sentence))
