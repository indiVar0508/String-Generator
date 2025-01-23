import random
from dna import DNA

class Population:
	def __init__(self, populationSize = 50, string = "this is default string", mutation = 0.01):
		self.populationSize = populationSize 
		self.string = string
		self.bestScore = 0
		self.best = ''
		self.totalScore = 0
		self.mutation = mutation
		self.generation = 0
		self.population = self.buildPopulation()
		self.matingPool = []


	def evolve(self):
		self.fitness()
		self.naturalSelection()
		self.generate()

	def optimized_evolve(self):
		self.fitness()
		self.optimized_generate()

	def getBest(self):
		return self.best

	def naturalSelection(self):
		self.matingPool = []
		maxFitness = 0
		for p in self.population:
			if p.fitness > maxFitness: 
				maxFitness = p.fitness

		for p in self.population:
			score = int((p.fitness / maxFitness) * 100)
			while score > 0:
				self.matingPool.append(p)
				score -= 1

	def generate(self):
		self.population = []
		for _ in range(self.populationSize):
			p1, p2 = self.matingPool[random.randint(0,len(self.matingPool)-1)], self.matingPool[random.randint(0,len(self.matingPool)-1)]
			child = DNA.cross_over(p1, p2)
			child.mutate()
			self.population.append(child)
		self.generation+=1

	def pickSomeone(self):
		index = random.randint(0, self.populationSize-1)
		r = random.random()
		while r > 0:
			r -= self.population[index].fitness
			index = (index + 1) % self.populationSize
		return self.population[index - 1]


	def optimized_generate(self):
		for p in self.population: p.probability = p.fitness / self.totalScore
		while len(self.population) != len(self.matingPool): 
			parentOne = self.pickSomeone()
			parentTwo = self.pickSomeone()
			child = DNA.cross_over(parentOne, parentTwo)
			child.mutate()
			self.matingPool.append(child)

		self.population = self.matingPool
		self.matingPool = []
		self.generation += 1
		


	def buildPopulation(self):
		temp = [DNA(self.string, self.mutation) for _ in range(0, self.populationSize)]
		return temp

	def matched(self):
		for _ in range(self.populationSize): 
			if self.population[_].evolved(): 
				self.best = self.population[_].string
				return True
		return False

	def fitness(self):
		maxfit = 0.4
		for _ in range(self.populationSize): 
			self.totalScore += self.population[_].set_fitness()
			if self.population[_].fitness > maxfit:
				self.best = self.population[_].string
				maxfit = self.population[_].fitness
				self.bestScore = maxfit


if __name__ == '__main__':
	p = Population(500)
	#p.naturalSelection()


