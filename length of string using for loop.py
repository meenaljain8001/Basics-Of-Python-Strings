# To find number of characters in a string 

str = input("enter a string : ")

i= 0 
for s in str:
    print(str[i], end=' ')
    i=i+1
    
print('\n number of characters :', i)
