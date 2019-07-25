from Population import *
import matplotlib.pyplot as plt

class geneticAlgo:
	def __init__(self,pop_size = 1500,string = "Hello woeld jhwpsmlwd dlwd", mutation = 0.01):
		self.p = Population(pop_size, string, mutation)
		self.scores = []

	def evolve(self):
		while not self.p.matched():
			self.p.evolve()
			#self.p.optimized_evolve()
			print('Generation : ',self.p.generation,' Best ->',self.p.getBest(),' target -> ',self.p.population[0].target,' best Score ->',self.p.bestScore)
			self.scores.append(self.p.bestScore)
		print('Generation taken : ',self.p.generation,' Target was  ->',self.p.getBest())
		plt.plot(range(self.p.generation), self.scores)
		plt.show()

if __name__ == '__main__':
	g = geneticAlgo()
	g.evolve()