class Gene:
    """Model class for Gene"""
    def __init__(self, geneData):
        self.geneSymbol = geneData['symbolOfGene']
        self.geneScore = geneData['score']
        self.geneInitialYear = geneData['yearInitial']
        self.geneFinalYear = geneData['yearFinal']
    
    def __str__(self):
        return f"Disease info: symbol: {self.geneSymbol}, score: {self.geneScore}, initial year: {self.geneInitialYear}, final year: {self.geneFinalYear}"