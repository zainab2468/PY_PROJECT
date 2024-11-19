#list of number
list = [2, 4, 7, 13, 9]

for i in list:
    print(i)



#maximum and minimum
list = [9, 7, 15, 3, 10, 19]
minimum = list[0] 

for i in list:
    if i < minimum:
        minimum = i
print("The smallest number in the list is :",minimum)

maximum = list[0]          #minimum
for i in list:
    if i > maximum:
        maximum = i
print("The largest number in the list is:", maximum)


