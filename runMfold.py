# In[run mffold automaticly, mfold produces around 10-20 files per input, make new folder per run]:

import os
#becarefull, laptop can handle only so much, do it one per time not all at the same time, if so go to the peregrine.'''
SeqList = os.popen('ls -p /home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/llmg_0079 | grep -v /').read().split()
#make folder for each .fas with the results of mfold in them.'''
print(os.getcwd())
os.chdir("/home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/llmg_0079")
print(os.getcwd())
for i in range(len(SeqList)):
    os.mkdir('/home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/llmg_0079/{0}'.format(SeqList[i].replace(".fas","")))
    os.chdir("/home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/llmg_0079/{0}".format(SeqList[i].replace(".fas","")))
    print(os.getcwd())
    os.popen("mfold SEQ='/home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/llmg_0079/{0}' T=30".format(SeqList[i]),'w')
    os.chdir("/home/manager/Bioinformatics-Project-Ribofind/Riboswitch_sequences/llmg_0079")
    print(os.getcwd())

