# Car Salesman
print("Please input your car's sale:")
car_sale = int(input())
tax_sale = 0.1*car_sale
tag_sale = 0.1*car_sale
print("Please input your cost of labor:")
labor_sale = int(input())
print("Please input your cost of trans:")
trans_sale = int(input())
total = car_sale + tax_sale + tag_sale + labor_sale + trans_sale
print("The total fees of your car is", total)