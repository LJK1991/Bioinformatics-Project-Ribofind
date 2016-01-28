# In[make a list from the loci tags found in the Riboswitch csv and search them in the complete genome file so the gene sequences can be put together]:

import os
LocusList=os.popen('cut -f 5 /home/flucas/Documents/Bioinformatics/week3/Startfile/Riboswitches\ Lucas.csv').read().split()

LocusFile = open('LocusFile.txt', 'w')
print(len(LocusList))

for locus in range(1, len(LocusList)):
    Locustag = os.popen('agrep -d "\>" -B -y -0 {0} /home/flucas/Documents/Bioinformatics/week3/sequence.txt'.format(LocusList[locus])).read()
    LocusFile.write(Locustag)
    print(locus, LocusList[locus])

LocusFile.close()

