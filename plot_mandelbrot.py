import complex_numbers.py
import colorsys
from PIL import Image


def is_in_mandelbrot(z,num_iter):
	curr = z
	prev = Complex()
	for i in range(num_iter):
		curr = add_complex(z,square_complex(prev))
		prev = curr

		if(curr.abs() > 2):
			return False, i
	return True


def to_rgb(i): 
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5)) 
    return tuple(color.astype(int)) 


def plot_mandelbrot(height,width,num_iter,image):
	pixels = image.load()
	for x in range(image.size[0]):
		for y in range(image.size[1]):
			state = is_in_mandelbrot(Complex((x - (0.75 * width))/(width/4),(y - (width/4))/(width/4)),num_iter)
			if type(state) != type(tuple()):
				pixels[x,y] = (0,0,0)
			else:
				pixels[x,y] = to_rgb(state[1])
