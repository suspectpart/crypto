import math
import random

def number_ones_and_zeros(x):
	difference = math.fabs(x.count(0) - x.count(1))
	tolerance = math.sqrt(len(x))
	success =  difference <= tolerance

	print "Zeros: ", x.count(0), ", Ones: ", x.count(1)
	print "Difference #0(x) - #1(x): ", difference
	print "Threshold difference: ", tolerance
	print "-> test ok\n" if success else "-> test failed\n"
	return success

def consecutive_zeros(x):
	consecutive_zeros = 0
	threshold = 10 * math.sqrt(len(x))
	for i, v in enumerate(x):
		if i < (len(x) - 1) and x[i] == 0 and x[i+1] == 0:
			consecutive_zeros = consecutive_zeros + 1
	success = consecutive_zeros - (len(x) / 4) <=  threshold

	print "#Consecutive Zeros(x): ", consecutive_zeros
	print "Threshold #Consecutive Zeros: ", threshold + len(x) / 4
	print "-> test ok\n" if success else "-> test failed\n" 
	return success

def longest_zero_run(x):
	counter = longest = 0
	threshold = 10 * math.log(10, 2)
	for bit in x:
		counter = counter + 1 if bit == 0 else 0
		longest = counter if counter > longest else longest
	success = longest <= threshold
	print "Max zero run: ", longest
	print "Threshold: ", threshold 
	print "-> test ok\n" if success else "-> test failed\n"
	return success

if __name__ == "__main__":
	random_bits = [random.getrandbits(1) for bit in range(0,1000000)]
	number_ones_and_zeros(random_bits)
	consecutive_zeros(random_bits)
	longest_zero_run(random_bits)