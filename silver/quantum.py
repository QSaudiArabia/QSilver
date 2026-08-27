import random, math
from numpy import arcsin
from math import pi

# randomly create a 2-dimensional quantum state
def random_quantum_state():
	first_entry = random.randrange(101)
	first_entry = first_entry/100
	first_entry = first_entry**0.5 
	if random.randrange(2) == 0: 
		first_entry = -1 * first_entry
	second_entry = 1 - (first_entry**2)
	second_entry = second_entry**0.5
	if random.randrange(2) == 0: 
		second_entry = -1 * second_entry
	return [first_entry,second_entry]
	
# randomly create a 2-dimensional quantum state	
def random_quantum_state2():
	angle_degree = random.randrange(360)
	angle_radian = math.pi * angle_degree / 180
	return [math.cos(angle_radian),math.sin(angle_radian)]	
	
# finding the angle of a 2-dimensional quantum state
def angle_quantum_state(x,y):
	angle_radian = math.acos(x) # radian of the angle with state |0>
	angle_degree = 360*angle_radian/(2*math.pi) # degree of the angle with state |0>
	# if the second amplitude is negative, 
	#     then angle is (-angle_degree)
	#     or equivalently 360 + (-angle_degree)
	if y<0: angle_degree = 360-angle_degree # degree of the angle
	# else degree of the angle is the same as degree of the angle with state |0>
	return angle_degree	
	
def state_to_angles(current_quantum_state):
	theta = 2*arcsin(round(abs(current_quantum_state[1]), 4))
	if(current_quantum_state[0] == 0 or current_quantum_state[1] == 0):
		phi = 0
	else:
		a_prime = current_quantum_state[0]/abs(current_quantum_state[0])
		angle_lambda = arcsin(abs(a_prime.imag))
		if(a_prime.real < 0 and a_prime.imag >= 0):
			angle_lambda = pi - angle_lambda
		if(a_prime.real < 0 and a_prime.imag < 0):
			angle_lambda = pi + angle_lambda
		if(a_prime.real >= 0 and a_prime.imag < 0):
			angle_lambda = 2*pi - angle_lambda
		b_prime = current_quantum_state[1]/abs(current_quantum_state[1])
		angle_nju = arcsin(abs(b_prime.imag))
		if(b_prime.real < 0 and b_prime.imag >= 0):
			angle_nju = pi - angle_nju
		if(b_prime.real < 0 and b_prime.imag < 0):
			angle_nju = pi + angle_nju
		if(b_prime.real >= 0 and b_prime.imag < 0):
			angle_nju = 2*pi - angle_nju
		phi = angle_nju - angle_lambda
	return [theta, phi]