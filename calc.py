class Calculator:
	def _init_(self):
		pass

	def add(self, x, y):
		return x+y
	
	def sub(self, x, y):
		return x-y
cal = Calculator()
print(cal.add(2,3))
print(cal.sub(5,2))
