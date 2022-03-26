def calc_newborn_gene(parent1_gene,parent2_gene):
    #if the genes are different one of them is dominant so the newborn will have it
    if parent1_gene != parent2_gene:
        return parent1_gene.upper()
    #if the genes are equal we return one of them
    else:
        return parent1_gene