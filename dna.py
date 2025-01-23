import random
import string

class DNA:
	def __init__(self, target = "this is default string", mutation = 0.01):
		self.target = target
		self.len = len(self.target)
		self.string = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=self.len))
		self.mutation = mutation
		self.fitness = 0.0
		self.probability = 0.0

	def mutate(self) -> None:
		temp = list(self.string)
		for i in range(0, len(temp)):
			if random.uniform(0, 1) < self.mutation:
				temp[i] = random.choices(string.ascii_lowercase+ string.punctuation + ' ')[0]
		self.string = ''.join(temp)

	@classmethod
	def cross_over(cls, parent_one: 'DNA', parent_two: 'DNA') -> 'DNA':
		child = DNA(parent_one.target, parent_one.mutation)
		midPoint = random.randint(0,parent_one.len-1)
		l = list(child.string)
		for i in range(len(l)):
			if i < midPoint: l[i] = parent_one.string[i]
			else: l[i] = parent_two.string[i]
		child.string = ''.join(l)
		return child

	def set_fitness(self):
		count = 0
		for i in range(self.len):
			if self.string[i] == self.target[i]: count += 1
		self.fitness =  count / self.len
		return self.fitness

	def evolved(self):
		return self.string == self.target


if __name__ == '__main__':
	pass


