string = input("Enter a long string : ")
search = input("Enter searchble string : ")
string=string.split(" ")
count=0
for i in string:
    if(i == search):
        count=count+1
print(count)

