food_amount=float(input('Enter the your food amount Rs:'))
food_percentage=float(input('Enter the tip percentage %:'))/100
tip_amount=food_amount*food_percentage
total=food_amount+tip_amount
print('-------------------------------------')
print(f'Food amount Rs={food_amount}')
print(f'Tip amount Rs={tip_amount}')
print(f'Total amount Rs={total}')
print('-------------------------------------')
