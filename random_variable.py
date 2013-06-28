''' 
a random variable is a function that distributes 
all values in the universe U to a space of V
'''

def distribution(universe, random_variable):
	results = [random_variable(u) for u in universe]
	v = {}

	for result in results:
		v[result] = v[result] + 1 if result in v else 1

	for key in v.iterkeys():
		print key, ":", float(v[key])  / len(results)

if __name__ == "__main__":
	universe = [1,2,3,4,5,6]
	random_variable = lambda x: "even" if x % 2 == 0 else "odd"
	distribution(universe, random_variable)
	print "\n"
	distribution(universe, lambda x: x ** 2)
	print "\n"
	distribution(universe, lambda x: x / 2)