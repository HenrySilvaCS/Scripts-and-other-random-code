import numpy as np 

class Complex:

	def __init__(self,real = 0,imaginary = 0):
		self.real = real 
		self.imaginary = imaginary 

	def abs(self):
		return np.sqrt(np.power(self.real,2) + np.power(self.imaginary,2))

	def find_theta(self):
		self.theta = np.arcsin(self.imaginary/np.sqrt(np.power(self.real,2) + np.power(self.imaginary,2)))
		return self.theta 

	def __repr__(self):
		return "Complex()"

	def __str__(self):
		return f"{self.real} + {self.imaginary}i"


def add_complex(z1,z2):
	assert type(z1) == type(Complex())
	assert type(z2) == type(Complex())

	z3 = Complex()

	z3.real = z1.real + z2.real 
	z3.imaginary = z2.imaginary + z1.imaginary
	return z3


def square_complex(z):
	z2 = Complex()
	z2.real = np.power(z.real,2) - np.power(z.imaginary,2)
	z2.imaginary = 2 * z.real * z.imaginary

	return z2 
