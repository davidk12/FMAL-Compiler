"""Lexer Class"""
import sys
import re
from Token import Token

class Lexer:
	def __init__(self):
		self.input = sys.stdin.read()
		self.input = re.sub(r'\s', '', self.input)
		
	def nextToken(self):
		if len(self.input)== 0 or self.input == None:
			return;
		tok = Token("", "")
		char = self.getChar()
		self.removeChar()
		self.addChar(char, tok)
		
		if char != None:
			if char.isdigit():
				for c in self.input:
					char = self.getChar()
					if char.isdigit():
						self.removeChar()
						self.addChar(char, tok)
					else:
						break
			elif char.isalpha():
				for c in self.input:
					if tok.lexeme == "print":
						tok.tCode = "PRINT"
					elif tok.lexeme == "end":
						tok.tCode = "END"
					else:
						char = self.getChar()
						if char.isalpha():
							self.removeChar()
							self.addChar(char, tok)
						else:
							break
			else:
				if self.isOneCharToken(char) == False:
					char = self.getChar()
					self.addChar(char, tok)
		self.lookUp(tok)
		
		return tok
				
	def getChar(self):
		char = ""
		if len(self.input) > 1:
			char = self.input[0];
			return char
		elif len(self.input)  == 1:
			char = self.input[0];
			return char
		else:
			return char
			
	def removeChar(self):
		if len(self.input) > 1:
			self.input = self.input[:0] + self.input[1:]
		elif len(self.input)  == 1:
			self.input = []
		else:
			return
			
	def addChar(self, char, tok):
		if char != None:
			tok.lexeme+=char
		
	def lookUp(self, tok):
		if tok.lexeme == "print":
			tok.tCode = "PRINT"
		elif tok.lexeme == "end":
			tok.tCode = "END"
		elif tok.lexeme == "(":
			tok.tCode = "LPAREN"
		elif tok.lexeme == ")":
			tok.tCode = "RPAREN"
		elif tok.lexeme == "*":
			tok.tCode = "MULT"
		elif tok.lexeme == "-":
			tok.tCode = "MINUS"
		elif tok.lexeme == "+":
			tok.tCode = "PLUS"
		elif tok.lexeme == ";":
			tok.tCode = "SEMICOL"
		elif tok.lexeme == "=":
			tok.tCode = "ASSIGN"
		else:
			matchID = re.match("^[A-Za-z]+$", tok.lexeme)
			matchINT = re.match("^[0-9]+$", tok.lexeme)
			
			if matchID:
				tok.tCode = "ID"
			elif matchINT:
				tok.tCode = "INT"
			else:
				tok.tCode = "ERROR"
	def isOneCharToken(self, char):
		if char == "(":
			return True
		elif char == ")":
			return True
		elif char == "*":
			return True
		elif char == "-":
			return True
		elif char == "+":
			return True
		elif char == ";":
			return True
		elif char == "=":
			return True
		else:
			return False