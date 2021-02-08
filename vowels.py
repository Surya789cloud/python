wor=input("enter")
v=['a','e','i','o','u']
listt=[]
for x in wor:
    if(x in v and x not in listt):
        listt.append(x)
        print("vowels are",listt)
    