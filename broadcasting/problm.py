prices=[100,200,300]

discount=10

final01=[]

for price in prices:
    final=price -(price*discount/100)
    final01.append(final)

print(final01)