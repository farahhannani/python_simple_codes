print ("Item 1")
name_item1 = input ("Name of the item : ")
quantity1 = int(input("Numbers of bought item : "))
price1 = float(input("Price for the item (RM) : "))

print ("Item 2")
name_item2 = input ("Name of the item : ")
quantity2 = int(input("Numbers of bought item : "))
price2 = float(input("Price for the item (RM) : "))

print ("Item 3")
name_item3 = input ("Name of the item : ")
quantity3 = int(input("Numbers of bought item : "))
price3 = float(input("Price for the item (RM) : "))

print ("Item 4")
name_item4 = input ("Name of the item : ")
quantity4 = int(input("Numbers of bought item : "))
price4 = float(input("Price for the item (RM) : "))

item1_total = quantity1 * price1
item2_total = quantity2 * price2
item3_total = quantity3 * price3
item4_total = quantity4 * price4

total  = ( quantity1 * price1 ) + ( quantity2 * price2 ) + ( quantity3 * price3 ) + ( quantity4 * price4 )
payment = 150.00


print ("Total = ",round(total,2))
print ("Payment = ",round(payment,2))
print("--------------------------------------------------")

print("Your receipt")
print(name_item1 + "\tRM" + str(item1_total))
print(name_item2 + "\tRM" + str(item2_total))
print(name_item3 + "\t\tRM" + str(item3_total))
print(name_item4 + "\t\tRM" + str(item4_total))
print("Total \t\tRM" + str(total))
print("--------------------------------------------------")

print("Cash \t\tRM"+str(payment))
print ("Change due \tRM"+str(round(payment-total,2)))
print("Thank you for shopping at PCS Store!")