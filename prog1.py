#Name-Suryakant Prashant Parida
#Reg no-12114784
#ph no-8484024856
#mail id-paridasuryakant1818@gmail.com
products = {
    'Leather':[1100,18,1],
    'Umbrella': [900,12,2],
    'Cigarette': [200,28,3],
    'Honey':[100,0,4]

}
lst=[]
# printing the total amount to be paid by the shopkeeper
total_price = 0
for i in products.values():
    product_price1 = i[0]*i[2]
    lst.append(i[1])
   
   
    if i[0] >= 500:
        product_price1 = product_price1 - (0.05 * product_price1)
    product_price1 = product_price1 + (i[1]*product_price1)
    total_price += product_price1
    
print("total_price of product", total_price)
print("maximum GST",max(lst))