from population import Population
try:
	import matplotlib.pyplot as plt
	show_vis = True
except ImportError:
	# doesn't want visualization
	show_vis = False

class StringGenerator:
	def __init__(self,pop_size = 1500,string = "wubba lubba dub dub!!!?!><!", mutation = 0.01):
		self.p = Population(pop_size, string, mutation)
		self.scores = []

	def evolve(self):
		while not self.p.matched():
			self.p.evolve()
			#self.p.optimized_evolve()
			print('Generation : ',self.p.generation,' Best ->',self.p.get_best(),' target -> ',self.p.population[0].target,' best Score ->',self.p.best_score)
			self.scores.append(self.p.best_score)
		print('Generation taken : ',self.p.generation,' Target was  ->',self.p.get_best())
		if show_vis is True:
			plt.plot(range(self.p.generation), self.scores)
			plt.show()
			plt.savefig("plot.png")

if __name__ == '__main__':
	g = StringGenerator()
	g.evolve()