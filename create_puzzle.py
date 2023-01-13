import random


def create_puzzle(words, n):
	puzzle = [[] for _ in range(n)]
	# puzzle is a list containing n lists so far
	for m in range(n):
		for _ in range(n):
			# append n spaces to each sub-list in puzzle
			puzzle[m].append(' ')

	for word in words:
		# use for loop to get each word from words
		while True:
			# the boolean veriable intersected is used indicate whether or not
			# the word will intersect other words that already placed 
			intersected = False
			if random.randint(0, 1) == 1:
				# place the word vertically
				starting = [
					random.randint(0, n - 1), # horizontal coordinate of starting point
					random.randint(0, n - len(word))] # vertical coordinate
				
				for y in range(starting[1], starting[1] + len(word)):
					# the horizontal coordinate fixed for vertical placement
					# hence use for loop to get a series of vertical coordinate
					# for each letter of the current word
					# len() is used to get correct range of y
					# (avoiding "index out of range" error)
					if puzzle[y][starting[0]] != ' ':
						# use y and starting[0] as indexes of puzzle
						# to get the value of the cell that will be placed a letter
						# if the cell is not a space
						# it means the word will intersect with previous words
						intersected = True
						break
				if intersected:
					# go to the beginning of the while loop
					# and try other starting point
					continue
				
				# start placing the word if intersected is false
				for y in range(starting[1], starting[1] + len(word)):
					# get a series of vertical coordinate (horizontal coordinate is fixed)
					puzzle[y][starting[0]] = word[y - starting[1]]
				# break will end the while loop
				# and the outer for loop will get the next word in words
				break
			
			else:
				# place the word horizontally
				# this part is similar to the part shown above
				starting = [
					random.randint(0, n - len(word)),
					random.randint(0, n - 1)]
				
				for x in range(starting[0], starting[0] + len(word)):
					if puzzle[starting[1]][x] != ' ':
						intersected = True
						break
				if intersected:
					continue
				
				for x in range(starting[0], starting[0] + len(word)):
					puzzle[starting[1]][x] = word[x - starting[0]]
				break

	return puzzle

# test the function
words = [
	"formula",
	"function",
	"calculus",
	"proof",
	"equation"
]
n = 10
puzzle = create_puzzle(words, n)
for row in puzzle:
	print(row)
input()