# In[reformat the newly combined.fas file and split them into seperate .fas files, mfold can handle only seq at a time.]:

import os
import re
import fileinput

FasFileList=os.popen('ls /home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences').read().split()

for i in range(len(FasFileList)):
    f = fileinput.input('/home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/{0}'.format(FasFileList[i]))
    LineList=[]
    for line in f :
        LineList.append(line)
    f.close()
    CurrentFile = open('/home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/{0}'.format(FasFileList[i]), 'w')
    SearchString = r'(\>).{4}(\w+).+?[tag]+\=(\w+).+?(\d+)\.\.(\d+).+?([\-\+]).(\d+).(\d+).(\d+)'
    SubString = r'\1\2|\3|gene:\4-\5|5-UTR:\7-\8|\6|\9'
    NewString = re.sub(SearchString,SubString,LineList[0])
    print(NewString)
    CurrentFile.write(LineList[0].replace(LineList[0],NewString))
    CurrentFile.write(LineList[1])
    LineList.clear()
    CurrentFile.close()
