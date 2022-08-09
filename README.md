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
***Reproducibility Instructions:***

1: Download a default environment of Python 3: https://www.python.org/downloads/

2: Due to GitHub file size constraints, download all supplementary data at (ZENODO LINK)

3: Place "1-output.txt" (the raw output from our Boa queries) and "5-cc_output.txt" (the output from previous work's classifier on our dataset (https://github.com/tkdsheep/TechnicalDebt/tree/master/src)) into the python_scripts folder in this GitHub repository. All other data from Zenodo is for replication comparison only.

4: Run the Python scripts in the python_scripts folder in numerical order. After the execution of each script, a numbered output file will be produced that is used in a later script. These files are also in our Zenodo repository as well, so users can compare their reproduced output with the output used in our study to verify reproducibility. The broad results from these steps are stated in Table 1 of our paper.
