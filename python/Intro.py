# PocketMoney = int (input('enter the pocket you get : '))

# if(PocketMoney>500):
#     print("You are a Rich Kid")
# elif(PocketMoney>100):
#     print("U have a good Life")
# else:
#     print("I Know What U feel")

# count = 500
# while(count>=0):
#     print(count)
#     count=count-1

introString = input("Enter String : ")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount = characterCount+1
    if(i==" "):
        wordCount=wordCount+1
print("Number of Word of the string :-")
print(wordCount)
print("Number of Character of the string :-")
print(characterCount)