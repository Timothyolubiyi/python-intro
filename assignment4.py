4.#Mrs Bridget went to market she bought the following items from the market
#Pawpaw 200 pieces @50 per one
#Ginger.                     500 @5 each
#Groundnut              50  @10 each
#Stationeries            450 @ 10 per one
#Stationeries            450 @ 10 per one
#Bread for the kids  10 pieces @ 50 each
#If she had 10000 in her account but she can only spend 75% of this amount nothing #more
#Now the question: .
#Write python code that determines how much does mrs Bridget has left off the 75%


pawpaw=200*50
ginger=500*5
groundnut=50*10
stationeries=450*10
bread=10*50
cash=10000
expenses=pawpaw+ginger+stationeries+bread
print(expenses)

avail_amount=(10000)*75/100
reserve_amount=(10000)*25/100
amount_left=10000-avail_amount
print(" The amount left is: ", amount_left)

