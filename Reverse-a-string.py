str=input("Plese enter your own string:")

str2 = ('')

#loop for printing in reverse

for i in str:
    str2 = i + str2

    #hello
    # 1 -> str2 = h + ' ' 
    #2 ->  str2 = e + h
    #3 -> str2 = l + eh
    #4 -> str2 = l + leh
    #5 -> str2 = o + lleh

print("\n original string = ", str)
print("the reversed string=",str2)
