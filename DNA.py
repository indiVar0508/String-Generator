import random
import string
class DNA:
	def __init__(self, target = "this is default string", mutation = 0.01):
		self.target = target
		self.len = len(self.target)
		self.string = self.makeString()
		self.mutation = mutation
		self.fitness = 0.0
		self.probability = 0.0


	def makeString(self):
		s = ''.join(random.choices(string.ascii_letters+ string.punctuation + ' ', k=self.len))
		return s

	def mutate(self):
		temp = list(self.string)
		for i in range(0, len(temp)):
			if random.uniform(0, 1) < self.mutation:
				temp[i] = random.choices(string.ascii_lowercase+ string.punctuation + ' ')[0]
		self.string = ''.join(temp)

	def crossOver(self, parentTwo):
		child = DNA(self.target, self.mutation)
		midPoint = random.randint(0,self.len-1)
		l = list(child.string)
		for i in range(len(l)):
			if i < midPoint: l[i] = self.string[i]
			else: l[i] = parentTwo.string[i]
		child.string = ''.join(l)
		#print(self.string,parentTwo.string,child.string)
		return child

	def setFitness(self):
		count = 0
		for i in range(self.len):
			if self.string[i] == self.target[i]: count += 1
		self.fitness =  count / self.len
		return self.fitness

	def matched(self):
		return self.string == self.target


if __name__ == '__main__':
	pass


