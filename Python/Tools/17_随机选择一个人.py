import random

class Eng:

	def __init__(self):
		self.engteam=["Rex Wang", "Nathan Lu", "Hugo Xu", "Ansel Liu", "Carlos Luo","Ema Qin","Rain Dai","Ida Ding","Min Yang","Xiaoqi Shi"]

	def sort(self):
		print("随机选择到：", random.choice(self.engteam))

people=Eng()
people.sort()

