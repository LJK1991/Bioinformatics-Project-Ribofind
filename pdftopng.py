# In[convert all pdf results to png, pygame cant display pdf]:

import os

FoldList = os.popen('ls -p /home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/llmg_0079 | grep /').read().split()


for i in range(len(FoldList)):
    os.chdir("/home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/llmg_0079/{0}".format(FoldList[i]))
    pdfList = os.popen('ls | grep pdf').read().split()
    if len(pdfList) == 0:
        continue
    else:
        for j in range(len(pdfList)):
            os.popen('pdftoppm -png -scale-to-x 591 -scale-to-y 800 {0} {1}'.format(pdfList[j], pdfList[j].replace('.pdf', '')))
    print("done")
