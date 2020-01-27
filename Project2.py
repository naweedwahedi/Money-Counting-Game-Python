
penny_Value = 1
nickel_Value = 5
dime_Value = 10
quarter_Value = 25
dollar_Value = 100

print("\nMoney Counting Game")
pennies = int (input("Enter the number of pennies: "))
nickels = int (input("Enter the number of nickels: "))
dimes = int (input("Enter the number of dimes: "))
quarters = int (input("Enter the number of quarters: "))

penny_total = pennies * penny_Value
nickel_total = nickels * nickel_Value
dime_total = dimes * dime_Value
quarter_total = quarters * quarter_Value

total = penny_total +nickel_Value + dime_total + quarter_total

if total == dollar_Value:
    print ("Congratulations! That combination of coins makes a dollar!")
elif total > dollar_Value:
    total = total / 100
    print("\nSorry,",total,"is more than a dollar")
else: 
    print("\nSorry",total,"is less than a dollar")