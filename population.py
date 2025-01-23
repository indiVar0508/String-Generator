import random
from copy import deepcopy
from dna import DNA

class Population:
	def __init__(self, population_size = 50, taget_string = "this is default string", mutation = 0.01):
		self.population_size = population_size 
		self.target_string = taget_string
		self.best_score = 0
		self.best = ''
		self.total_score = 0
		self.mutation = mutation
		self.generation = 0
		self.population = self.build_population()
		self.mating_pool = []


	def evolve(self):
		self.fitness()
		self.natural_selection()
		self.generate()

	def optimized_evolve(self):
		self.fitness()
		self.optimized_generate()

	def get_best(self):
		return self.best

	def natural_selection(self):
		self.mating_pool = []
		best_candidate = max(self.population, key=lambda x: x.fitness)

		for p in self.population:
			score = int((p.fitness / best_candidate.fitness) * 100)
			while score > 0:
				self.mating_pool.append(p)
				score -= 1

	def generate(self):
		self.population = []
		for _ in range(self.population_size):
			p1, p2 = self.mating_pool[random.randint(0,len(self.mating_pool)-1)], self.mating_pool[random.randint(0,len(self.mating_pool)-1)]
			child = DNA.cross_over(p1, p2)
			child.mutate()
			self.population.append(child)
		self.generation+=1

	def pick_someone(self):
		index = random.randint(0, self.population_size-1)
		r = random.random()
		while r > 0:
			r -= self.population[index].fitness
			index = (index + 1) % self.population_size
		return self.population[index - 1]


	def optimized_generate(self):
		for p in self.population: p.probability = p.fitness / self.total_score
		while len(self.population) != len(self.mating_pool): 
			parentOne = self.pick_someone()
			parentTwo = self.pick_someone()
			child = DNA.cross_over(parentOne, parentTwo)
			child.mutate()
			self.mating_pool.append(child)

		self.population = deepcopy(self.mating_pool)
		self.mating_pool = []
		self.generation += 1

	def build_population(self):
		temp = [DNA(self.target_string, self.mutation) for _ in range(0, self.population_size)]
		return temp

	def matched(self):
		for _ in range(self.population_size): 
			if self.population[_].evolved(): 
				self.best = self.population[_].string
				return True
		return False

	def fitness(self):
		max_fit = 0.0
		for i in range(self.population_size): 
			self.total_score += self.population[i].set_fitness()
			if self.population[i].fitness > max_fit:
				self.best = self.population[i].string
				max_fit = self.population[i].fitness
				self.best_score = max_fit


if __name__ == '__main__':
	p = Population(500)
	#p.naturalSelection()


