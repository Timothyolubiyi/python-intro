

2.#Mr Thomas has four properties valued at 100,000  each 
#his father gave him 50,000 
#his mum gave him 150,000 
#He bought a car at a value of  200,000 
#he gave his wife 30,000, 
# if the money in his account initially is 2,000000
#Write a python code that will show how much he has in his account
#Name the file assigment2.py



prop_valued=100000*4
father=50000
mum=150000
car_pur=200000
wife=30000
init_bal=2000000
cash_gift=father+mum
print("Total cash gift is: ", cash_gift)
total_bal=cash_gift+init_bal-wife-car_pur
print("The total balance is: ", total_bal)
