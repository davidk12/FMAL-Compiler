"""Compiler Class"""
from Lexer import Lexer
from Parser import Parser

class Compiler:
	def main(self):
		myLexer = Lexer()
		myParser = Parser(myLexer)
		myParser.parse()
c = Compiler()
c.main()
