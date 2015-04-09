"""Parser Class"""
import sys
from Lexer import Lexer
from Token import Token

class Parser:
#Constructor
	def __init__(self, lexer):
		self.__lex = lexer
		self.__tok = Token("", "")
	
#public class functions	
	#parse
	def parse(self):
		self.__nextTok()
		self.__Statements()
	
#private class functions	
	#Statements
	def __Statements(self):
		if self.__tok.tCode == "END":
			sys.exit();
		else:
			self.__Statement()
			if self.__tok.tCode == "SEMICOL":
				self.__nextTok()
				self.__Statements()
			else:
				self.__error()
	
	#Statement
	def __Statement(self):
		if self.__tok.tCode == "ID":
			print("PUSH "+self.__tok.lexeme)
			self.__nextTok()
			if self.__tok.tCode == "ASSIGN":
				self.__nextTok()
				self.__Expr()
				print("ASSIGN")
			else:
				print(self.__tok.tCode)
				self.__error()
		elif self.__tok.tCode == "PRINT":
			self.__nextTok()
			if self.__tok.tCode == "ID":
				print("PUSH "+self.__tok.lexeme)
				print("PRINT")
				self.__nextTok()
			else:
				self.__error()
		else:
			self.__error()
	
	#Expr
	def __Expr(self):
		self.__Term()
		if self.__tok.tCode == "PLUS":
			self.__nextTok()
			self.__Expr()
			print("ADD")
		if self.__tok.tCode == "MINUS":
			self.__nextTok()
			self.__Expr()
			print("SUB")
	
	#Term
	def __Term(self):
		self.__Factor()
		if self.__tok.tCode == "MULT":
			self.__nextTok()
			self.__Term()
			print("MULT")
	
	#Factor
	def __Factor(self):
		if self.__tok.tCode == "INT":
			print("PUSH "+self.__tok.lexeme)
			self.__nextTok()
		elif self.__tok.tCode == "ID":
			print("PUSH "+self.__tok.lexeme)
			self.__nextTok()
		elif self.__tok.tCode == "LPAREN":
			self.__nextTok()
			self.__Expr()
			if self.__tok.tCode == "RPAREN":
				self.__nextTok()
			else:
				self.__error()
		else:
			self.__error()
	
	#lex
	def __nextTok(self):
		self.__tok = self.__lex.nextToken()
		if self.__tok.tCode == "ERROR":
			self.__error()
	
	#error	
	def __error(self):
		print("Syntax error!")
		sys.exit()
		