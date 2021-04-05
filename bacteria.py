class bacteria():
    """
    Bacteria class
    
    Bacteria has a location (x, y) and genes array. 
    Has a mitosis function with mutation rate
    """
    
    def __init__(self, x=0, y=0, mutation_rate=0.1):

        self.genes = np.random.rand(3)
        self.loc = (x, y)
        self.mutation_rate = mutation_rate
    
    def mitosis(self):
        new = bug(mutation_rate=self.mutation_rate)
        for (i, g) in enumerate(self.genes):
            if random.random() > self.mutation_rate:
                newbug.genes[i] = self.genes[i]
        return newbug
    
    def draw(self):
        """Draws the bug with rgb color corresponding to it's genes."""
        plt.scatter(self.loc[0], self.loc[1], color=self.genes)