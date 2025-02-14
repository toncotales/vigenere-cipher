# ===================================================================
# MIT License
#
# Copyright (c) 2025 Anthony Cotales
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ===================================================================

import string
import random


class VigenereCipher:

	def __init__(self):
		self.alphabet = self.random_alphabet()
		self.table = self.generate_table()

	def random_alphabet(self):
		alphabet = list(string.ascii_letters)
		random.shuffle(alphabet)
		return ''.join(alphabet)

	def generate_table(self):
		table = []
		for i in range(len(self.alphabet)):
			row = self.alphabet[i:] + self.alphabet[:i]
			table.append(row)
		return table

	def cipher(self, plaintext, key) -> str:
		ciphertext = []
		key_index = 0
		for char in plaintext:
			if char in self.alphabet:
				row = self.alphabet.index(char) # Get row index
				column = self.alphabet.index(key[key_index % len(key)])
				ciphertext.append(self.table[row][column])
				key_index += 1
			else:
				# Non-alphabetic characters remain unchanged
				ciphertext.append(char)
		return ''.join(ciphertext)

	def decipher(self, ciphertext, key) -> str:
		plaintext = []
		key_index = 0
		for char in ciphertext:
			if char in self.alphabet:
				row = self.alphabet.index(key[key_index % len(key)])
				column = self.table[row].index(char)
				plaintext.append(self.alphabet[column])
				key_index += 1
			else:
				# Non-alphabetic characters remain unchanged
				plaintext.append(char)
		return ''.join(plaintext)