class Calculator:
	def _init_(self):
		pass

	def add(self, x, y):
		return x+y
	
	def sub(self, x, y):
		return x-y

	def multiply(self, x, y):
		return x*y

	def divide(self, x,y):
		return x/y
cal = Calculator()
print(cal.add(2,3))
print(cal.sub(5,2))
print(cal.multiply(6,3))
print(cal.divide(6,3))
