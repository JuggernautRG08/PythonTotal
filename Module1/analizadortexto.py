text = input("Input your text file: ")
words = []
text=text.lower()
words.append(input("Enter the first letter to search for: ").lower())
words.append(input("Enter the second letter to search for: ").lower())
words.append(input("Enter the third letter to search for: ").lower())

print ("\n")
print ("number of letters entered: ")
letters_number1 = text.count(words[0])
letters_number2 = text.count(words[1])
letters_number3 = text.count(words[2])

print(f"We have found the letter: '{words[0]}', repeat {letters_number1} times")
print(f"We have found the letter: '{words[1]}', repeat {letters_number2} times")
print(f"We have found the letter: '{words[2]}', repeat {letters_number3} times")


print ("\n")
print ("Number of words")
number_words=text.split()
print (f"We have finned: {len(number_words)} words in your text file")
print(f"the first letter in your text file is: '{text[0]}', and the final letter is: '{text[-1]}')")
