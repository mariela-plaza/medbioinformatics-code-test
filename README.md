# Disease and gene command utility

The disease and gene command utility is a command line developed with Python with two functionalities for retrieving information about diseases and genes.

It was developed with the DISGENET plus API.

## Requirements

To use the disease and gene command utility, you need the following:

- python3
- An API Key for the DISGENET plus API

## Instalation

You can install the disease and gene command utility in two ways:

### 1. Using the github repository:

Go to the github repository github.com/mariela-plaza/medbioinformatics-code-test and clone it to your computer with the following command line:

```bash
git clone https://github.com/mariela-plaza/medbioinformatics-code-test.git
```

Install the dependencies of the project with the following command line:

```bash
pip install -r requirements.txt
```

You are ready now to make use of the disease and gene command utility as shown in the usage section of this file.

### 2. Using the .zip file

Unpack the.zip file in a place on your computer. Once that is done, go to the most inner main-1.0 directory and install the dependencies of the project with the following command line:

```bash
pip install -r requirements.txt
```

You are ready now to make use of the disease and gene command utility as shown in the usage section of this file.

## Usage

1. Enter your API Key for the DISGENET plus API in the apiKey.json file in place of the placeholder "TYPE_YOUR_API_KEY"

```json
{
  "apiKey": "TYPE_YOUR_API_KEY"
}
```

2. From the command line, you can use the command line app as follows:

```bash
# For the disease data type the command line above, substituting the DISEASE_IDENTIFIER
# with an UMLS disease code. Examples: C0036341, C0002395, C0013264
python3 main.py disease DISEASE_IDENTIFIER
```

```bash
# For the gene data type the command line above, substituting the GENE_HGNC_SYMBOL
# with an HGNC gene symbol. Examples: PRDX1, AGPAT5, LCLAT1
python3 main.py gene GENE_HGNC_SYMBOL
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
