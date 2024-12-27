
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
print("-------------录入规格要求-------------")
#rated_speed=round(float(input("额定转速是多少rpm？")),2)
rated_torque_spec=round(float(input("额定扭矩规格是多少oz.in？")),2)
#rated_amps_spec=round(float(input("额定电流规格是多少A？")),2)
#rated_watt_in_spec=round(float(input("额定输入功率规格是多少W？")),2)
#no_load_amps_spec=round(float(input("空载电流规格是多少？")),2)
#no_Load_watt_in_spec=round(float(input("空载输入功率规格是多少？")),2)
#stall_torque_spec=round(float(input("堵转扭矩规格是多少？")),2)
#stall_watt_in_spec=round(float(input("堵转功率规格是多少W？")),2)

print("-------------录入实测数据-------------")
torque=round(float(input("实测额定扭矩是多少oz.in？")),2)
#rated_amps=round(float(input("实测额定电流是多少A？")),2)
#rated_watt_in=round(float(input("实测额定输入功率是多少W？")),2)
#no_load_amps=round(float(input("实测空载电流是多少？")),2)
#no_Load_watt_in=round(float(input("实测空载输入功率是多少？")),2)
#stall_torque=round(float(input("实测堵转扭矩是多少？")),2)
#stall_watt_in=round(float(input("实测堵转功率是多少W？")),2)

#print("-------------计算规格上下限度-------------")15

rated_torque_spec_up=round(float(rated_torque_spec*1.1),2)
rated_torque_spec_low=round(float(rated_torque_spec*0.9),2)
#rated_amps_spec_up=round(float(rated_amps_spec*1.1),2)
#rated_amps_spec_low=round(float(rated_amps_spec*0.9),2)
#rated_watt_in_spec_up=round(float(rated_watt_in_spec*1.1),2)
#rated_watt_in_spec_low=round(float(rated_watt_in_spec*0.9),2)
#no_load_amps_spec_up=round(float(no_load_amps_spec*1.1),2)
#no_load_amps_spec_low=round(float(no_load_amps_spec*0.9),2)
#no_load_watt_in_spec_up=round(float(no_Load_watt_in_spec*1.1),2)
#no_load_watt_in_spec_low=round(float(no_Load_watt_in_spec*0.9),2)
#stall_torque_spec_up=round(float(stall_torque_spec*1.1),2)
#stall_torque_spec_low=round(float(stall_torque_spec*0.9),2)
#stall_watt_in_spec_up=round(float(stall_watt_in_spec*1.1),2)
#stall_watt_in_spec_up=round(float(stall_watt_in_spec*0.9),2)

print("-------------判断实测数据是否在规格内，以及如何处理-------------")
print(f"额定扭矩规格为{rated_torque_spec_low}-{rated_torque_spec_up}oz.in")
print(f"实测扭矩为{torque}oz.in")
if rated_torque_spec_low <= torque <=rated_torque_spec_up:
	print(f"{GREEN}实测额定扭矩 {torque} oz.in 在规格 {rated_torque_spec_low}-{rated_torque_spec_up}oz.in内，判定为合格.{RESET}")
elif torque<rated_torque_spec_low:
	a=rated_torque_spec_low-torque
	b="{:.2f}%".format(a/rated_torque_spec_low * 100)
	if float(b[:-1])<5:
		print(f"{YELLOW}额定扭矩超过规格下限{b}，可以让步接收{RESET}")
	else:
		print(f"{RED}额定扭矩超过规格下限{b}，不能让步接收，需查找原因，并返工。{RESET}")
elif torque>rated_torque_spec_up:
	c = torque-rated_torque_spec_low
	d = "{:.2f}%".format(c / rated_torque_spec_up* 100)
	if float(d[:-1])<5:
		print(f"{YELLOW}额定扭矩超过规格上限{d}，可以让步接收{RESET}")
	else:
		print(f"{RED}额定扭矩超过规格上限{d},不能让步接收，需查找原因，并返工。{RESET}")


