"""
print("--------------------------美元转人名币和欧元------------------------------")
f = int(input("Please input the usd: "))
exchange_rate3 =7.2628
exchange_rate4 =0.9224
g = round(f*exchange_rate3,2)
h = round(f*exchange_rate4,2)
print("the USD：", f," is equal to:")
print(g,"RMB")
print(h,"Euro")
"""

print("--------------------------人名币转美元和欧元------------------------------")
c = int(input("Please input the RMB: "))
exchange_rate3 =0.1378
exchange_rate4 =0.1261
d = round(c*exchange_rate3,2)
e = round(c*exchange_rate4,2)
print("the RMB：", c," is equal to:")
print( d,"USD")
print(e,"Euro")

'''
print("--------------------------欧元转美元和人名币------------------------------")
a = int(input("Please input the euro: "))
exchange_rate1 =1.09
exchange_rate2 =7.91
b = round(a*exchange_rate1,2)
c = round(a*exchange_rate2,2)
print("the euro：", a,"is equal to:")
print( b,"USD")
print(c,"RMB")
'''