# In[make a new .fas file from the two .fas files that were created that were made with regex Locustag1 and Locustag2]:

import csv
import os

LocusList=os.popen('cut -f 5 /home/manager/Bionformatics-Project-Ribofind/Startfile/Riboswitches\ Lucas.csv').read().split()
LocusList.pop(0)

L2file = open('/home/manager/Bionformatics-Project-Ribofind/Locusfile2.txt', 'r')
L1file = open('/home/manager/Bionformatics-Project-Ribofind/LocusFile.txt', 'r')

L2List = L2file.readlines()
L1List = L1file.readlines()

print(len(L1List), len(L2List), len(LocusList))
os.mkdir('/home/manager/Bionformatics-Project-Ribofind/Riboswitch_sequences')
for i in range(0,len(L1List),2):
    newfile = open("/home/manager/Bionformatics-Project-Ribofind/Riboswitch_sequences/{0}.fas".format(LocusList[i//2]), 'w')
    newfile.write(L1List[i].replace("\n",""))
    newfile.write(L2List[i])
    newfile.write(L2List[i+1].replace("\n",""))
    newfile.write(L1List[i+1])
    newfile.close()

L1file.close()
L2file.close()
