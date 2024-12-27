coff="Coffee machine"
cube="Suger cube"
bean="Coffee beans"
water="Water"
clean="Machined cleaned"
tank="Tanker clean"
milk="Milk"
list=[coff,cube,bean,water,clean,tank,milk]
def Check(coff):
	a= input(f'+Does the "{coff}" ready?')
	if "y" in str.lower(a):
		print(f'---Great, the "{coff}" "is ready.')
		return True
	else:
		print(f'---Please be sure the" {coff} "is ready')
		return False
list2=[]
print("========================Checking List========================")
for i in list:
	b=Check(i)
	if b==True:
		list2.append("Ready🙂")
	else:
		list2.append("Not Ready🤣")
print()
print("========================Checking Result========================")
for i in range(len(list)):
	print("---",list[i],":",list2[i])
print()
print("========================What's Next========================")
if "Not Ready🤣" in list2:
	print("Be sure all above are ready before to use it.")
else:
	print("Enjoy the coff, wise you have a great day. ;)")

