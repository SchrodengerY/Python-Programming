# 编写一个能够计数的程序，让用户输入起始数字，结束数字以及计数的步长。

print("This is a programe for counting.\n")
ini_num = int(input("Please input the initial number: "))
end_num = int(input("Please input the end number: "))
step = int(input("Please input the step: "))

if ini_num > end_num:
	print("Please correct your initial number to insure the initial number is no more than end number!\n")
	ini_num = int(input("The corrected initial number: "))
if step > (end_num-ini_num):
	print("Please shrink the step.\n")
	step = int(input("The corrected step: "))
for item in range(ini_num,end_num,step):
	print(item)

# 倒序输出
str = input("Please enter what you like:")
for item in range(len(str),0,-1):
	print(item,end='')
print("\n")

