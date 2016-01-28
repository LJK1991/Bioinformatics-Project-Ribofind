# In[changed and improved my old .py script. to mimic polymerase split the sequences into 1 per base, to increase order make a seperate folder for these split files and assign them a number]:

import os
import re

LocusList = os.popen('ls -p /home/flucas/Documents/Bioinformatics/week3/Riboswitch_sequences | grep -v /' ).read().split()

for i in range(len(LocusList)): 
    CurrentFile = open('/home/flucas/Documents/Bioinformatics/week3/Riboswitch_sequences/{0}'.format(LocusList[i]), 'r')
    os.mkdir('/home/flucas/Documents/Bioinformatics/week3/Riboswitch_sequences/{0}'.format(LocusList[i].replace('.fas','')))
    LineList = CurrentFile.readlines()
    Header = re.search('.+\|(\d+)', LineList[0])
    UTRLen = Header.group(1)
    for j in range(1, 51+int(UTRLen)):
        newfile = open('/home/flucas/Documents/Bioinformatics/week3/Riboswitch_sequences/{0}/{1}'.format(LocusList[i].replace('.fas',''), LocusList[i].replace(".fas", "-{0:0>3}.fas".format(j))), 'a')
        newfile.write(LineList[0].replace("\n","\t") + "Base: {0} to {1}\n".format(0, j))
        newfile.write(LineList[1][0:j].replace("T","U"))
        newfile.close()
    print(LocusList[i], " is done")
    LineList.clear()
    CurrentFile.close()
