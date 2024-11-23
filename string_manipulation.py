#reversing a string
word = "was it a cat i saw"
#reverse = word[::1] #this doesn't work
print(reverse)

reverse = word[::-1] #the minus sign 



#counting vowels in string
word = "Irritability" 
vowel = "aeiouAEIOU"
count = 0

for i in word:
    if i in vowel:
      count += 1

print(count)




#Replacing word in sentence
word = "Welcome back home Christopher"
new = word.replace("Christopher", "Alfred")
print(new)
