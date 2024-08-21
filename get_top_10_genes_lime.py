import re
from collections import Counter, defaultdict


def parse_sample_data(sample_data):
    genes_conditions = re.findall(
        r'(ENSG\d+)(.*?)([><]=?)\s*(-?\d*\.\d+)', sample_data)
    return [(gene, 'positive' if '>' in operator else 'negative') for gene, _, operator, _ in genes_conditions]


def process_samples(filename):
    gene_status = defaultdict(lambda: {'positive': 0, 'negative': 0})

    with open(filename, 'r') as file:
        for line in file:
            _, sample_data = line.split(':', 1)
            genes = parse_sample_data(sample_data)
            for gene, status in genes:
                gene_status[gene][status] += 1

    return gene_status


def get_top_10_genes(gene_status):
    sorted_genes = Counter(
        {gene: counts['positive'] + counts['negative'] for gene, counts in gene_status.items()})
    top_10_genes = sorted_genes.most_common(10)

    top_10_status = [(gene, 'positive' if gene_status[gene]['positive'] >= gene_status[gene]['negative'] else 'negative')
                     for gene, _ in top_10_genes]

    return top_10_status


def display_results(top_10_status):
    print("Top 10 Features:")
    for gene, status in top_10_status:
        print(f"  Gene: {gene}, Predominant Status: {status}")


filename = 'lime_features.txt'
gene_status = process_samples(filename)
top_10_status = get_top_10_genes(gene_status)
display_results(top_10_status)
