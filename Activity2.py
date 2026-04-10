var = "Hello"
for i in var:
    print(i)



#Count vowels in a string

word = input("Give me a string and I will count the vowels in the word for you")

count = 0

for i in word:
    if i.lower() in "aeiou":
        count = count + 1

print(f"There are {count} of vowels in your word")


#Reverse the string

word = input("Give me a word and I will reverse it for you")

reverse = ''

for i in word:
    reverse = i + reverse


print(reverse)

#In while loop

word = input("Give me a word and I will reverse it for you")

reverse = ''

var = 0

while(var < len(word)):
    reverse = word[var] + reverse
    var = var + 1
    #var is going to be the index

#Find the sum of first 10 numbers

nums = 10

count = 0

for i in range(1 , nums + 1):
    count = count + i

print(count)

#count how many even and odd numbers from the given input range of numbers(take 2 input n1 and n2 consider that as range) and also the sum of even and odd for the same

n1 = int(input("GIve me a start number for a range"))
n2 = int(input("Give me for a end for the range "))



#count words in a sentence

#check whether given input string is a palindrome or not.  (palindrome means when u reverse the word remains the same)

