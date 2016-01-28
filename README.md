# Bioinformatics-Project-Ribofind
#Bioinformatics course project

Finding riboswitches in Lactococcus lactis subsp. cremoris MG1363
Currently 24 Riboswitches are know, many riboswitch finding algorithms try to find new ones by homology search.
although this is usefull across species it is unlikely to find completely new riboswitches. this project aims at finding new riboswitches
not based on the conserverd functional aptamer, but by the expression platform, containg the regulatory terminator. 
to find this i though that a mimic of polymerase might be usefull, as it comes closer to what happens in reality. instead of what most people
have used before by inputting the full RNA seq. this should show a terminator folding around the end -'3 end of the sequence.
by using additional terminator search algorithm these are easier to find.

additonal programs and modules:
mfold-3.6 --> http://unafold.rna.albany.edu/?q=mfold/download-mfold
pygame --> http://www.pygame.org/hifi.html note* if using py3 make sure you have v1.9.2 pre

first few .py scripts are for reformatting the starting files i had.
collectingGeneseq.py
splittingfas.py

