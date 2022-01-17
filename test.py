import unittest
from models import Gene
from utils import Response

class TestGene(unittest.TestCase):
    def test_gene_table(self):
        gene = Gene({'symbolOfGene': 'GNAC', 'score': 0.9, 'yearInitial': 1978, 'yearFinal': 2007})
        gene_table_data = gene.create_table_info()
        expected_result = ['GNAC', 0.9, 1978, 2007]

        self.assertEqual(gene_table_data, expected_result)
    
    def test_gene_table_with_none_values(self):
        gene = Gene({'symbolOfGene': None, 'score': None, 'yearInitial': None, 'yearFinal': None})
        gene_table_data = gene.create_table_info()
        expected_result = [None, None, None, None]

        self.assertEqual(gene_table_data, expected_result)

    def test_gene_instantiation_with_missing_properties(self):
        gene_missing_data = Gene({'symbolOfGene': 'GNAC', 'yearInitial': 1978, 'yearFinal': 2007})
        expected_result = None

        self.assertEqual(gene_missing_data.gene_score, expected_result)

class TestResponse(unittest.TestCase):
    def test_get_gene_variants(self):
        response = Response({'payload': [{"geneToVariants":[{'varStr': 'ex1'}, {'varStr': 'ex2'}, {'varStr': 'ex3'}]}]})
        gene_variants_data = response.get_gene_variants()
        expected_result = [{'varStr': 'ex1'}, {'varStr': 'ex2'}, {'varStr': 'ex3'}]

        self.assertEqual(gene_variants_data, expected_result)

    def test_get_gene_variants_with_no_variants(self):
        response = Response({'payload': [{"geneToVariants":[]}]})
        gene_variants_data = response.get_gene_variants()
        expected_result = []

        self.assertEqual(gene_variants_data, expected_result)

if __name__ == '__main__':
    unittest.main()