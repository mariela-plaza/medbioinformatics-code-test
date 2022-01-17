class Gene:
    """Model class for Gene"""
    def __init__(self, gene_data):
        self.gene_symbol = gene_data.get('symbolOfGene', None)
        self.gene_score = gene_data.get('score', None)
        self.gene_initial_year = gene_data.get('yearInitial', None)
        self.gene_final_year = gene_data.get('yearFinal', None)

    def create_table_info(self):
        gene_table_info = [self.gene_symbol, self.gene_score, self.gene_initial_year, self.gene_final_year];
        return gene_table_info
