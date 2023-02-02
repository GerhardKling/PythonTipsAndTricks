"""
Select a point P inside the square of length q randomly (2D).
1. Each point P is the centre of a circle of radius r.
2. Circle must be inside the square.
3. Circle are not permitted to overlap.
4. Determine the probability of drawing a point in N draws, which is the centre of a permitted circle.
"""

import numpy as np
import random

#Parameters
q = 100
r = 5
N = 1000

#Increments
inc = 1/1000

#Random draw in range 0 to q, excluding boundaries
def random_draw(q, inc):
	return round(random.randint(1, q/inc)*inc, 3)

#Points in 2D
all_points = []
inside_points = []
valid_points = []
for _ in range(N):
	#Draw point P
	P = (random_draw(q, inc),random_draw(q, inc))
	all_points.append(P)
	#Check condition 1: inside square
	inside = False
	if P[0] > r and P[0] < q-r and P[1] > r and P[1] < q-r:
		inside = True
	if inside:
		inside_points.append(P)

#Check condition 2
if len(inside_points) > 0:
	for idx, point in enumerate(inside_points):
		#First point inside square fulfills condition 2
		if idx == 0:
			valid_points.append(point)
		else:
			valid = True
			for v_point in valid_points:
				if np.sqrt((point[0]-v_point[0])**2+(point[1]-v_point[1])**2)<2*r:
					valid = False
			if valid:
				valid_points.append(point)
else:
	print("No circle is inside the square.")

#Point after N draws
print(inside_points)

print(f"{len(inside_points)} of {N} points are inside the square.")

print(all_points)

print(f"\n{len(valid_points)} of {N} points are valid.")

prob = len(valid_points)/N

print(f"\nThe probability to draw a valid point is {prob}.")