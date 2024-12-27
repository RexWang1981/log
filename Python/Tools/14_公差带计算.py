#EngTeam=["Rex","Nathan","Carlos", "Ida", "Ema","Min", "Ansel","Hugo","Rain","Xiaoqi"]
#print(EngTeam.count("Rex")) #count统计数组中某个值出现的次数
#print("技术部人数:",len(EngTeam))

up = float(input("Please input upper limit in inch:\n"))
lo = float(input("Please input lower limit in inch:\n"))
up = round(up*25.4,4)
lo = round(lo*25.4,4)
print("The upper limit is:", up, "mm")
print("The lower limit is:", lo, "mm")
print("The tolerance range is：", lo, "to", up,"mm")
data = float(input("Please input measured data in :\n"))
if lo <= data <= up:
	print("OK,\n it meet the spec, it is acceptable")
else:
	print("NG,\n it can not meet the spec, need to reject or ask for deviation.")

def tol(mid,up,low, unit):
	mid=input()