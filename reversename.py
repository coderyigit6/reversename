#making new function
def reverseword(word):
	#send the reversed version of the word
	return word[::-1]
	
#take input from user
text=input("please type something to be reversed: ")
#use the reverseword funcion to print the input to the display 
print(reverseword(text))