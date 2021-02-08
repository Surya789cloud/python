def find_leap(year):
    count=0
    leap_years=[]    
    while(count<y):
        if(year%400==0 or (year%4==0 and year%100!=0)):
            leap_years.append(year)
            count=count+1
        year=year+1
    return leap_years
y=int(input())
leap_list=find_leap(y)
print(leap_list)