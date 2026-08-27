import matplotlib.pyplot
from matplotlib.pyplot import figure,gca
from matplotlib.patches import Arc
from math import sin,cos,pi
from qiskit.visualization import plot_bloch_vector, bloch
from matplotlib.pyplot import text
from qutip import *

def draw_axes():
	points = [ [1.2,0], [0,1.2], [-1.2,0], [0,-1.2] ] # dummy points for zooming out
	arrows = [ [1.1,0], [0,1.1], [-1.1,0], [0,-1.1] ] # coordinates for the axes
	for p in points: 
		matplotlib.pyplot.plot(p[0],p[1]+0.1) # drawing dummy points
	for a in arrows: 
		matplotlib.pyplot.arrow(0,0,a[0],a[1],head_width=0.04, head_length=0.08) # drawing the axes


def draw_unit_circle():
	unit_circle= matplotlib.pyplot.Circle((0,0),1,color='black',fill=False)
	matplotlib.pyplot.gca().add_patch(unit_circle) 

	
def draw_quantum_state(x,y,name):
	# shorten the line length to 0.92
	# line_length + head_length should be 1
	x1 = 0.92 * x
	y1 = 0.92 * y
	matplotlib.pyplot.arrow(0,0,x1,y1,head_width=0.04,head_length=0.08,color="blue")
	x2 = 1.15 * x
	y2 = 1.15 * y
	matplotlib.pyplot.text(x2,y2,name)
	
def draw_qubit():
	# draw a figure
	matplotlib.pyplot.figure(figsize=(6,6), dpi=60)
	# draw the origin
	matplotlib.pyplot.plot(0,0,'ro') # a point in red color
	# drawing the axes by using one of our predefined function
	draw_axes()
	# drawing the unit circle by using one of our predefined function
	draw_unit_circle()
	# drawing |0>
	matplotlib.pyplot.plot(1,0,"o")
	matplotlib.pyplot.text(1.05,0.05,"|0>")
	# drawing |1>
	matplotlib.pyplot.plot(0,1,"o")
	matplotlib.pyplot.text(0.05,1.05,"|1>")
	# drawing -|0>
	matplotlib.pyplot.plot(-1,0,"o")
	matplotlib.pyplot.text(-1.2,-0.1,"-|0>")
	# drawing -|1>
	matplotlib.pyplot.plot(0,-1,"o")
	matplotlib.pyplot.text(-0.2,-1.1,"-|1>")
	
def draw_real_part():
	points = [ [1.2,0], [0,1.2] ] # dummy points for zooming out
	arrows = [ [1.1,0], [0,1.1] ] # coordinates for the axes
	for p in points: 
		matplotlib.pyplot.plot(p[0],p[1]+0.1) # drawing dummy points
	for a in arrows: 
		matplotlib.pyplot.arrow(0,0,a[0],a[1],head_width=0.04, head_length=0.08) # drawing the axes
	#gca().add_patch( Arc((0,0),2,2,angle=0,theta1=0,theta2=pi/2,color="black",linewidth=2) )
	# drawing |0>
	matplotlib.pyplot.plot(1,0,"o")
	matplotlib.pyplot.text(1.05,0.05,"|0>")
	# drawing |1>
	matplotlib.pyplot.plot(0,1,"o")
	matplotlib.pyplot.text(0.05,1.05,"|1>")
	
def draw_imaginary_part():
	# draw a figure
	matplotlib.pyplot.figure(figsize=(6,6), dpi=60)
	# draw the origin
	matplotlib.pyplot.plot(0,0,'ro') # a point in red color
	# drawing the axes by using one of our predefined function
	draw_axes()
	# drawing the unit circle by using one of our predefined function
	draw_unit_circle()
	# drawing 1
	matplotlib.pyplot.plot(1,0,"o")
	matplotlib.pyplot.text(1.05,0.05,"1")
	# drawing i
	matplotlib.pyplot.plot(0,1,"o")
	matplotlib.pyplot.text(0.05,1.05,"i")
	# drawing -1
	matplotlib.pyplot.plot(-1,0,"o")
	matplotlib.pyplot.text(-1.2,-0.1,"-1")
	# drawing -i
	matplotlib.pyplot.plot(0,-1,"o")
	matplotlib.pyplot.text(-0.2,-1.1,"-i")

def draw_bloch(theta, phi):
	x = sin(theta)*cos(phi)
	y = sin(theta)*sin(phi)
	z = cos(theta)
	# preparing the sphere
	sphere = bloch
	sphere.Bloch
	b = Bloch()
	# preparing the lables
	b.ylpos = [1.1, -1.2]
	b.xlabel = ['$\\left|0\\right>+\\left|1\\right>$', '$\\left|0\\right>-\\left|1\\right>$']
	b.ylabel = ['$\\left|0\\right>+i\\left|1\\right>$', '$\\left|0\\right>-i\\left|1\\right>$']
	# first 6 drawn vectors will be blue, the 7th - red
	b.vector_color = ['b','b','b','b','b','b','r']
	# drawing vectors of orthogonal states (most popular bases), note the coordinates of vectors,
	# they correspond to the according states.
	b.add_vectors([[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]])
	# drawing our state (as 7th vector)
	b.add_vectors([x,y,z])
	# showing the Bloch sphere with all that we have prepared
	b.show()

def draw_bloch2(theta, phi, theta2, phi2):
	x = sin(theta)*cos(phi)
	y = sin(theta)*sin(phi)
	z = cos(theta)
	x2 = sin(theta2)*cos(phi2)
	y2 = sin(theta2)*sin(phi2)
	z2 = cos(theta2)
	# preparing the sphere
	sphere = bloch
	sphere.Bloch
	b = Bloch()
	# preparing the lables
	b.ylpos = [1.1, -1.2]
	b.xlabel = ['$\\left|0\\right>+\\left|1\\right>$', '$\\left|0\\right>-\\left|1\\right>$']
	b.ylabel = ['$\\left|0\\right>+i\\left|1\\right>$', '$\\left|0\\right>-i\\left|1\\right>$']
	# first 6 drawn vectors will be blue, the 7th - green, the 8th - red.
	b.vector_color = ['b','b','b','b','b','b','g','r']
	# drawing vectors of orthogonal states (most popular bases), note the coordinates of vectors,
	# they correspond to the according states.
	b.add_vectors([[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]])
	# drawing our state (as 7th vector)
	b.add_vectors([x,y,z])
	b.add_vectors([x2,y2,z2])
	# showing the Bloch sphere with all that we have prepared
	b.show()