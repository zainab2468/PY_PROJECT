
dict = {"bukola" : 23, "rasford": 20, "ginnery": 26, "albert" :18}
name_check =input("enter a key in the dictionary: ")

if name_check in dict.keys():
    print(dict[name_check])
else:
    print("can't be found")

value = list(dict.values())
print(value)



