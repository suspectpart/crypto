import random

rounds = 1000
accumulated_samples_to_collision = 0

for i in range(rounds):
	samples = []

	while True:
		birthday = random.randint(0, 365)
		if not birthday in samples:
			samples.append(birthday)
		else:
			accumulated_samples_to_collision += len(samples)
			samples = [] 
			break

print "On average it took ",  accumulated_samples_to_collision / float(rounds), " samples to have a collision."