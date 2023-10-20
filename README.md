# 23Shades
Artifact for the ESEC/FSE paper "23 Shades of Self-Admitted Technical Debt: An Empirical Study on Machine Learning Software"

This Artifact is split up as such: the labeling process, data processing scripts, and final data used in our study is present on this GitHub repository. Due to GitHub file restraints, the output from each intermediary step in our process is available for reproducibility comparison on Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7033365.svg)](https://doi.org/10.5281/zenodo.7033365)

This Artifact is organized as follows: \
\
***boa_scripts***: the scripts used to pull comment change data from a Boa dataset. When running scripts on the Boa website, the dataset used in this study can be found in the drop-down menu under the name "Jan/ML-Verse". This dataset has 2,641 projects found on GitHub, containing 5,840,020,882 AST nodes from 1,465,477 revisions. Follow the instructions bellow to run the analysis on Boa dataset:

1. Navigate to "https://boa.cs.iastate.edu/" on a web browser
2. Click "User Login (MSR)" on the side bar
3. On the pulled up webpage, select "request a user" if a user has not been registered yet. Otherwise, login at the side bar.
4. Click "Run Examples" on the side bar once you are logged in.
5. Copy and paste the code from "get_comment_changes.boa" found in this repository's "boa_scripts" folder
6. At the bottom of the page find the drop-down bar for "Input Dataset (use the SMALL dataset when testing queries!)", select "2021 Jan/ML-Verse"
7. Click run program, depending on the dataset size, it might take a while to complete. Once the query is done, you can "View Job Output" or "Download Job Output" at the top of the screen.

NOTE: the ML-Verse dataset is very large, so when the authors were running "get_comment_changes.boa", the dataset had to be partitioned and ran many times (for example, in one run only the 
repositories whose star count in the range of 0-10 were run, then another run stars 11-20 were ran). In the current version of "get_comment_changes.boa", only repos with 10 stars are ran. Change 
line 49 to specify how you wish to partition a run of the query. Because partitioning can be a very time-expensive process, we have combined the results of all partitioned queries into "1-output.txt"
which can be found on at our Zenodo: "https://zenodo.org/record/6975843#.YwpTYnbMK71".

\
***data***: the data gathered and analyzed for the study. Included are the filtered comments by repository type, the commit length and AST diff data, and the results of our labeling process. \
\
***labeling_process***: contains each labeling author's results, and the labels agreed upon after discussion. \
\
***python_scripts***: the scripts used to filter our extracted dataset of source code comments. \
\
***Reproducibility Instructions:***

1. Download a default environment of Python 3: https://www.python.org/downloads/
2. Due to GitHub file size constraints, download all supplementary data at https://zenodo.org/record/7033365#.Yw1vbNPMK70
3. Place "1-output.txt" (the raw output from our Boa queries) and "5-cc_output.txt" (the output from previous work's classifier on our dataset (https://github.com/tkdsheep/TechnicalDebt/tree/master/src)) into the python_scripts folder in this GitHub repository. All other data from Zenodo is for replication comparison only.
4. Run the Python scripts in the python_scripts folder in numerical order. After the execution of each script, a numbered output file will be produced that is used in a later script. These files are also in our Zenodo repository as well, so users can compare their reproduced output with the output used in our study to verify reproducibility. The broad results from these steps are stated in Table 1 of our paper.
