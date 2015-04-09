import sys
import fileinput
"""Interpreter Class"""
class Interpreter:
	def __init__(self):
		self.code = []
		self.map = Map()
		self.stack = Stack(self.map)
		
	def main(self):
		for line in fileinput.input():
			self.code.append(line.strip().split('\n'))
		
		self.code.reverse()
		
		while not self.code == False:
			if not self.code:
				break
			line = self.code.pop()
			self.interpret(line)
	def error(self, op):
		print("Error for operator: " + op)
		
	def interpret(self, line):
		strLine = ''
		strLine = ' '.join(line)
		strLine = strLine.split(" ")
		if strLine[0] == "PUSH":
			self.stack.push(strLine[1])
		elif strLine[0] == "ADD":
			self.stack.add()
		elif strLine[0] == "SUB":
			self.stack.sub()
		elif strLine[0] == "MULT":
			self.stack.mult()
		elif strLine[0] == "ASSIGN":
			self.stack.assign()
		elif strLine[0] == "PRINT":
			self.stack.Print()
		else:
			self.error(strLine[0])
		
"""Stack Class"""
class Stack(list):
	def __init__(self, m):
		self.map = m
	
	def check_int(self, s):
		if s[0] in ('-'):
			return s[1:].isdigit()
		return s.isdigit()
	
	def isEmpty(self):
		return not self
		
	def push(self, op):
		self.append(op)
		
	def add(self):
		if self.isEmpty() == True:
			return
			
		var1 = self.pop()
		
		if self.isEmpty() == True:
			return
			
		var2 = self.pop()
		
		if self.check_int(var2) and self.check_int(var1):
			self.push(str(int(var2) + int(var1)))
		elif self.check_int(var2) and self.check_int(self.map.getByID(var1).getValue()):
			self.push(str(int(var2) + int(self.map.getByID(var1).getValue())))
		elif self.check_int(self.map.getByID(var2).getValue()) and self.check_int(var1):
			self.push(str(int(self.map.getByID(var2).getValue()) + int(var1)))
		elif self.check_int(self.map.getByID(var2).getValue()) and self.check_int(self.map.getByID(var1).getValue()):
			self.push(str(int(self.map.getByID(var2).getValue()) + int(self.map.getByID(var1).getValue())))
		else:
			self.error("ADD")
			
	def sub(self):
		if self.isEmpty() == True:
			return
		var1 = self.pop()
		
		var2 = self.pop()
			
		if self.check_int(var2) and self.check_int(var1):
			self.push(str(int(var2) - int(var1)))
		elif self.check_int(var2) and self.check_int(self.map.getByID(var1).getValue()):
			self.push(str(int(var2) - int(self.map.getByID(var1).getValue())))
		elif self.check_int(self.map.getByID(var2).getValue()) and self.check_int(var1):
			self.push(str(int(self.map.getByID(var2).getValue()) - int(var1)))
		elif self.check_int(self.map.getByID(var2).getValue()) and self.check_int(self.map.getByID(var1).getValue()):
			self.push(str(int(self.map.getByID(var2).getValue()) - int(self.map.getByID(var1).getValue())))
		else:
			self.error("SUB")
		
	def mult(self):
		if self.isEmpty() == True:
			return
		
		var1 = self.pop()
		
		var2 = self.pop()
		
		if self.check_int(var2) and self.check_int(var1):
			self.push(str(int(var2) * int(var1)))
		elif self.check_int(var2) and self.check_int(self.map.getByID(var1).getValue()):
			self.push(str(int(var2) * int(self.map.getByID(var1).getValue())))
		elif self.check_int(self.map.getByID(var2).getValue()) and self.check_int(var1):
			self.push(str(int(self.map.getByID(var2).getValue()) * int(var1)))
		elif self.check_int(self.map.getByID(var2).getValue()) and self.check_int(self.map.getByID(var1).getValue()):
			self.push(str(int(self.map.getByID(var2).getValue()) * int(self.map.getByID(var1).getValue())))
		else:
			self.error("MULT")
		
	def assign(self):
		if self.isEmpty() == True:
			return
			
		var1 = self.pop()
		
		var2 = self.pop()
		
		if self.map.lookUpByID(var1):
			if self.map.lookUpByID(var2):
				self.map.getByID(var1).setValue(self.map.getByID(var2).getValue())
				self.push(var2)
			else:
				self.map.getByID(var1).setValue(var2)
				self.push(var2)
		elif self.map.lookUpByID(var2):
			self.map.getByID(var2).setValue(var1)
			self.push(var1)
		elif var2.isdigit() == False:
			idVal = IdentifierValue(var2, var1)
			self.map.push(idVal)
			self.push(var2)
		else:
			self.error("ASSIGN")
			
	def Print(self):
		if self.isEmpty() == False:
			var = self.pop()
			if self.map.lookUpByID(var):
				print(self.map.getByID(var).getValue())
			else:
				print(var)
		else:
			self.error("PRINT")
	
	def error(self, op):
		print("Error for operator: " + op)
		
"""Map Class"""
class Map(list):
	def push(self, item):
		self.append(item)
		
	def isEmpty(self):
		return not self
		
	def lookUpByValue(self, value):
		for IDVal in self:
			if IDVal.VALUE == value:
				return True
		return False
		
	def lookUpByID(self, id):
		for IDVal in self:
			if IDVal.ID == id:
				return True
		return False
		
	def getByID(self, id):
		for IDVal in self:
			if IDVal.ID == id:
				return IDVal
				
	def getByValue(self, value):
		for IDVal in self:
			if IDVal.VALUE == value:
				return IDVal

"""IdentifierValue Class"""
class IdentifierValue:
	def __init__(self, id, value):
		self.ID = id
		self.VALUE = value
		
	def getID(self):
		return self.ID
		
	def getValue(self):
		return self.VALUE
	def setValue(self, value):
		self.VALUE = value
		
interpreter = Interpreter()
interpreter.main()