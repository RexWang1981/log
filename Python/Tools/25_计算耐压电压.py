v = int(input("请输入电机额定电压（单位V）:"))

if v <= 120:
	v=120
elif 120 < v <= 240:
	v=240
elif 240 < v <= 277:
	v=277

hipot=round((2.4*v +1200),0)

if hipot <= 1500:
	hipot=1500
elif 1500<hipot<=2000:
	hipot=2000
elif 2000< hipot <= 2500:
	hipot = 2500
elif 2500< hipot <= 3000:
	hipot = 2500
print("\n----------------耐压测试标准----------------")
print(f"▪耐压测试电压为:{hipot}V.")
print("▪持续时间为:1s.\n▪泄漏电流规格为:0.02mA~2mA. \n▪ACR灵敏度等级为:5.")
print("-------------------END-------------------")