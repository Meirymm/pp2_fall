def volume_sphere(r):
	return 4/3*3.14*r**3

radius = int(input())
volume = volume_sphere(radius)
print(volume)