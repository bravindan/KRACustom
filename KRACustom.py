#the program will calculate the custom duty that a customer has to pay for imported goods
#goods imported from US will be shipped by Amazon
#goods imported from China will be shipped by Alibaba
import time

print("Welcome to Custom duty calculator for KRA")
print('============================================')
#checks whether the user has entered an integer
try:
    
    platform = int(input("Please enter 1 for US based goods or 2 for China based goods: "))
    goods = int(input("Please enter the quantity of goods: "))
    amount = int(input("Enter the cost per good: "))
    
except ValueError:
    print("Oops! You entered a non-integer. Try again...")
#function to calculate the Charges based on the total amount of imported products and postage_fee
def customCharges(g, a):
    start_time = time.time() #calculate the start time of the program
    postage_fee = 1000 #assume that the postage fee, independent of the quantity or type of goods is 1000
    #calculate the total quantity to be taxed
    taxable_amount = g * a
    #check whether taxable income is above $150 (this will be subjected to custom tax)
    if taxable_amount > 0 and taxable_amount < 150:
        print("No custom charges incurred:")
        print("The postage fee is: ", postage_fee, " Ksh")
        total = postage_fee
        print('Total fees incurred: ',total, ' Ksh')
    else:
        custom_charges = 0.25 * taxable_amount #0.25 is the average custom duty charges deducted by KRA
        total = postage_fee + custom_charges
        print("Custom charges: ",custom_charges, " Ksh")
        print("Amount payable: ",total, " Ksh")
    end_time = time.time() # calculate the endtime of the program
    print("==================================")
    #total time taken
    print(f"Runtime of the program is {end_time - start_time} seconds")
 
if platform == 1:
    print("==================================")
    print('Amazon will do the shipping')
    customCharges(goods, amount)
    print("==================================")
elif platform == 2:
    print("==================================")
    print('Alibaba will do the shipping')
    customCharges(goods, amount)
    print("==================================")
else:
    print('The platform you selected does not exist. Try again')

