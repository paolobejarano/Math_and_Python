'''
The Collatz conjecture states that if a number is divided by 2 if its even, and is tripled and the result added to 1 if odd,
when repetead indefinitily, will always lead to the result of 1.
'''
def algorithm_sequence(j):
	sequence = []
	sequence.append(j)
	k = 0
	while True:
		if sequence[k] == 1:
			break
		else:
			if sequence[k] % 2 != 0:
				n = int(3*sequence[k] + 1)
			else:
				n = int(sequence[k] / 2)
			sequence.append(n)
		k = k + 1
	return sequence

number = int(input("Enter a number: "))
sequence = algorithm_sequence(number)
print("The sequence is", sequence)
if sequence[len(sequence)-1] == 1:
	print("The last number of the sequence is 1; thus, the Collatz conjecture is valid for the number",number)
else:
	print(number,"must be an invalid input for the algorithm. Or you had found solution to one of the most enduring math riddles")
