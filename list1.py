list=[10,20,30,40,50,60,80,90]
#print(sum(list))
total=0
for i in list:
    #print(i)
    total=total+i
print(total)
if total>500:
    p=total*50
    print("Alas is greater than 500:", p)
    
else:
    print("oh no is less than 500")
    p=-total-50
    

    
