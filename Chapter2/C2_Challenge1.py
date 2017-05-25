# 扔硬币
import random

tries = 1
front_number = 0
contrary_number = 0

while(tries <= 100):
	coin = random.randint(1,2)
	if(coin == 1):
		#print("正面")
		front_number += 1
	else:
		contrary_number += 1
	tries += 1

print("正面向上次数为:",front_number)
print("\n反面向上次数为:",contrary_number)
print("---------------游戏结束-------------\n")