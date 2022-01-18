import unittest
from models import Gene
from utils import Response

class TestGene(unittest.TestCase):
    def setUp(self):
        self.test_cases = {
            'gene_table': {'symbolOfGene': 'GNAC', 'score': 0.9, 'yearInitial': 1978, 'yearFinal': 2007},
            'gene_table_with_none_values': {'symbolOfGene': None, 'score': None, 'yearInitial': None, 'yearFinal': None},
            'gene_instantiation_with_missing_properties': {'symbolOfGene': 'GNAC', 'score': None, 'yearInitial': 1978, 'yearFinal': 2007}
        }
        self.expected_result = {
            'gene_table': ['GNAC', 0.9, 1978, 2007],
            'gene_table_with_none_values': [None, None, None, None],
            'gene_instantiation_with_missing_properties': ['GNAC', None, 1978, 2007]
        }

    def test_gene_table(self):
        gene_table_data = Gene(self.test_cases['gene_table']).create_table_info()
        self.assertEqual(gene_table_data, self.expected_result['gene_table'])
    
    def test_gene_table_with_none_values(self):
        gene_table_data = Gene(self.test_cases['gene_table_with_none_values']).create_table_info()
        self.assertEqual(gene_table_data, self.expected_result['gene_table_with_none_values'])

    def test_gene_instantiation_with_missing_properties(self):
        gene_missing_data = Gene(self.test_cases['gene_instantiation_with_missing_properties']).create_table_info()
        self.assertEqual(gene_missing_data, self.expected_result['gene_instantiation_with_missing_properties'])

class TestResponse(unittest.TestCase):
    def setUp(self):
        self.test_cases = {
            'get_gene_variants': {'payload': [{"geneToVariants":[{'varStr': 'ex1'}, {'varStr': 'ex2'}, {'varStr': 'ex3'}]}], 'status': 'OK'},
            'get_gene_with_no_variants': {'payload': [{"geneToVariants":[]}], 'status': 'OK'}
        }
        self.expected_result = {
            'get_gene_variants': [{'varStr': 'ex1'}, {'varStr': 'ex2'}, {'varStr': 'ex3'}],
            'get_gene_with_no_variants': []
        }

    def test_get_gene_variants(self):
        gene_variants_data = Response(self.test_cases['get_gene_variants']).get_gene_variants()
        self.assertEqual(gene_variants_data, self.expected_result['get_gene_variants'])

    def test_get_gene_with_no_variants(self):
        gene_variants_data = Response(self.test_cases['get_gene_with_no_variants']).get_gene_variants()
        self.assertEqual(gene_variants_data, self.expected_result['get_gene_with_no_variants'])

if __name__ == '__main__':
    unittest.main()