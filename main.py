import fire
from tabulate import tabulate

from utils import Request, Response

request = Request()

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
    if disease_response.status == 'OK': 
        associated_genes = disease_response.get_disease()
        if len(associated_genes) != 0:
            print(tabulate(associated_genes, headers=["Gene HGNC symbol", "Score", "Initial Year", "Final Year"]))
        else:
            print('The parameter you provided is incorrect / not in our database. Please, try with a new disease UMLS code')
    else:
        print('The request failed. Please try again')
    

def print_gene_information(gene_HGNC_symbol):
    """
    Returns the Gene HGNC symbol introduced and the number of variants associated with said gene. 
    :param gene_HGNC_symbol: HGNC symbol of the gene to search. Examples: PRDX1, AGPAT5, LCLAT1
    """

    gene_request = request.request_gene(gene_HGNC_symbol);
    gene_response = Response(gene_request.json())

    if gene_response.status == 'OK':
        number_of_variants = len(gene_response.get_gene_variants())
        if number_of_variants != 0:
            print(tabulate([[gene_HGNC_symbol, number_of_variants]], headers=["Gene Symbol", "Number of variants"]))
        else:
            print('The parameter you provided is incorrect / not in our database. Please, try with a new HGNC gene symbol')
    else:
        print('The request failed. Please try again')

if __name__ == "__main__":
    fire.Fire({
        "disease": print_disease_information,
        "gene": print_gene_information
    })