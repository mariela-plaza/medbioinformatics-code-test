import fire
from tabulate import tabulate

from utils import Request, Response

request = Request();

def print_disease_information(disease_id):
    """
    Returns the first 10 genes associated with the disease identified by the diseaseId provided.
    The results are organized by descending score. The information provided for each gene is:
        * Gene HGNC symbol
        * Score
        * Initial Year
        * Final Year
    :param disease_id: identifier of the disease to search. Examples: C0036341, C0002395, C0013264
    """

    disease_request = request.request_disease(disease_id)
    disease_response = Response(disease_request.json())
    associated_genes = disease_response.get_disease()
    print(tabulate(associated_genes, headers=["Gene HGNC symbol", "Score", "Initial Year", "Final Year"]))

def print_gene_information(gene_HGNC_symbol):
    """
    Returns the Gene HGNC symbol introduced and the number of variants associated with said gene. 
    :param gene_HGNC_symbol: HGNC symbol of the gene to search. Examples: PRDX1, AGPAT5, LCLAT1
    """

    gene_request = request.request_gene(gene_HGNC_symbol);
    gene_response = Response(gene_request.json())
    number_of_variants = len(gene_response.get_gene_variants())
    print(tabulate([[gene_HGNC_symbol, number_of_variants]], headers=["Gene Symbol", "Number of variants"]))

if __name__ == "__main__":
    fire.Fire({
        "disease": print_disease_information,
        "gene": print_gene_information
    })