import string
import random
from dna import DNA
from population import Population
try:
	import matplotlib.pyplot as plt
	show_vis = True
except ImportError:
	# doesn't want visualization
	show_vis = False

class StringGenerator:
	def __init__(self,pop_size = 1500,string = "wubba lubba dub dub!!!?!><3! baby", mutation = 0.01):
		self.string_to_gen = string
		self.p = Population(pop_size, string, mutation)
		self.evolved_scores = []
		self.random_scores = []

	def evolve(self):
		while not self.p.matched():
			self.p.evolve()
			#self.p.optimized_evolve()
			print('Generation : ',self.p.generation,' Best ->',self.p.get_best(),' target -> ',self.p.population[0].target,' best Score ->',self.p.best_score)
			self.evolved_scores.append(self.p.best_score)
		print('Generation taken : ',self.p.generation,' Target was  ->',self.p.get_best())

	def randomise(self):
		for _ in range(200):
			generated = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=len(self.string_to_gen)))
			self.random_scores.append(DNA.compute_fitness(generated, self.string_to_gen))
		

if __name__ == '__main__':
	g = StringGenerator()
	g.randomise()
	g.evolve()
	if show_vis is True:
		plt.plot(range(len(g.evolved_scores)), g.evolved_scores, label="evolved score")
		plt.plot(range(len(g.random_scores)), g.random_scores, label="random score")
		plt.legend()
		plt.show()

		plt.savefig("plot.png")