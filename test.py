from PascalX import genescorer
import os

Gscorer = genescorer.chi2sum(window=50000,varcutoff=0.95)
Gscorer.load_refpanel('/home/tom/PROGRAMMING/KGGRCh38/EUR.1KG.GRCh38',parallel=4)

from PascalX.genome import genome

G = genome()
# G.get_ensembl_annotation('biomart_GRCh38.tsv')

Gscorer.load_genome('biomart_GRCh38.tsv')

Gscorer.load_GWAS("/home/tom/Downloads/GCST90002218_buildGRCh37.tsv",rscol=0,pcol=1,header=True)

R = Gscorer.score_chr(chrs=[2, 12])
# R = Gscorer.score(['WDR12'])
# print(Gscorer.plot_Manhattan(R[0]))


top_ten = Gscorer.get_topscores(N=10)
print("top_ten: ", top_ten)


#no luck with Manhattan Plot yet..
m_plot = Gscorer.plot_Manhattan(R[0], labelList=['WDR12'])
if m_plot:
    m_plot = m_plot.save("/home/tom/Downloads/m_plot")
    with open ("/home/tom/Downloads/m_plot", 'w') as f: 
        m_plot = Gscorer.plot_Manhattan(R[0])
        f.write("m_plot")
    f.close()



# print(R)
print("done")