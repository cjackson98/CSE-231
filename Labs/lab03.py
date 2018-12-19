VOWELS = "aeiou"
#word = input("Enter a word ('quit' to quit): ")
# Error message used in Mimir test
#print("Can't convert empty string.  Try again.")
    
word="a"
while word != "quit":
    word = input("Enter a word ('quit' to quit): ")
    word=word.lower()
    y=0
    z=0
    if word[0] in VOWELS:
        word=word+"way"
        print(word)
        continue
    if word=="quit":
        break
    else:
        while word[0] not in VOWELS:
            if len(word)==1:
                break
            word=word+word[0]
            word=word[1:]
        word=word+"ay"
        print(word)
        #for x in word:
        #    var=x
        #    z=word.find("a" or "e" or "i" or "u" or "o")
        #    print(z)
        #    if word[z] in VOWELS:
        #        #print(word)
        #        word=word+word[:z]
        #        #print(word)
        #        word=word[z:]
        #        #print(word)
        #        word=word+"ay"
        #        #print(word)
        #        break
        #    y=+1