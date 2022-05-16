#reverse=input("Enter a word to reverse: ")
#for char in range(len(reverse) -1, -1, -1) : 
   # print(reverse[char],end="")
    #print("\n")


my_word=input("Enter your favourite word")
rev = ''
for i in my_word:
    rev = i + rev 
    print("\n before reversing the word is:",my_word)
    print("after reversing the word is:",rev)