# 23Shades
Artifact for the ESEC/FSE paper "23 Shades of Machine Learning Technical Debt: An Empirical Study"

This Artifact is organized as follows: \
\
***boa_scripts***: the scripts used to pull comment change data from a Boa dataset. The Boa scripts can be ran at https://boa.cs.iastate.edu/boa/. When running scripts on the Boa website, the dataset used in this study can be found in the drop-down menu under the name "Jan/ML-Verse". This dataset has 2,641 projects found on GitHub, containing 5,840,020,882 AST nodes from 1,465,477 revisions.\
\
***data***: the data gathered and analyzed for the study. Included are the filtered comments by repository type, the commit length and AST diff data, and the results of our labeling process. \
\
***labeling_process***: contains each labeling author's results, and the labels agreed upon after discussion. \
\
***python_scripts***: the scripts used to filter our extracted dataset of source code comments. \
\
***Reproducibility Instructions:*** Due to GitHub file size restraints, download the supplementary data at: https://drive.google.com/drive/folders/1RksJKHvUoj2Qq_px8n2Gje1Bk0TtO52F , then place "1-output.txt" (the raw output from get_comment_changes.boa) and "5-cc_output.txt" (the output from previous work's classifier (https://github.com/tkdsheep/TechnicalDebt/tree/master/src)) into the python_scripts folder. All other data in the Google Drive is for replication comparison only. Once both files are in python_scripts, run each script in the numerical order, each script will output a file used in a later script. All results from this process should be exactly as stated in Table 1 of the paper.

