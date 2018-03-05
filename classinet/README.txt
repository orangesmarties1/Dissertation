ClassiNet README.txt


# IMPORTANT: if you missed it in the main README.txt file, please be aware that the
# code contained in this folder will not run properly without the datasets, which were
# too large to include in the submission.


This directory contains all code pertaining to ClassiNets.
Useful methods are located in library scripts (/lib). These should not be run directly.
The non-core files are located in /helper-scripts and will not run properly if executed
from there if they use a library script. They are not necessary to use ClassiNet anyway,
so have only been included here for completeness.


The files developed here are designed to be executed independently, often with output
from one, being used in another. Here we outline the necessary order of execution for
the core files to achieve results in thesis.
Note: first set global configuration variables in 'config.py'.

# TARGET WORDS AND TRAINING DATA

1) 'get-frequent-words.py'
Requires: files containing pre-processed sentences for learning ClassiNet correlations.
Output: file listing words occurring in sufficient number of sentences (target word candidates).

2) 'select-target-words.py'
Requires: files containing pre-processed sentences, and file containing frequent words.
Output: file listing selected target words ('target-words.txt')

3) 'select-sentences-with-targets.py'
Requires: output from 1)
Output: file listing sentences containing some target word ('sentences-with.txt') and
file listing sentences not containing some target word ('sentences-out.txt')

4) 'get-data-train.py'
Requires: output from 1), 2)
Output: file for each target word containing their training dataset

5) 'get-feat-space.py'
Requires: output from 3)
Output: file containing most frequent features from target training sets


# CREATE CLASSINET GRAPH

6) 'agreement-cosine.py'
Requires: output from 5)
Output: file listing cosine similarities between each pair of target words (using their
weight vectors)

7) 'agreement-select-pairs.py'
Requires: output from 6), 7)
Output: file listing top related pairs

8) 'get-data-agreement.py'
Requires: output from 7)
Output: file for each pair of target words containing their individual agreement dataset

# TEST AND TRAIN PREDICTORS

9) 'predict_linear.py' or 'predict_rbf.py'
Requires: output from 8)
Output: predicted linear/rbf data for each target word

10) 'agreement-prediction.py'
Requires: output from 9)
Output: file listing directed edges with weights ('edged-directed.txt')

11) 'knn-graph.py'
Requires: output from 10)
Output: file listing k-nn edges (with given k)

# USE CLASSINET FOR FEATURE EXPANSION

12) 'expand-neighb-all2.py'
Requires: output from 11), file containing pre-processed sentences for target task 
Output: file containing expanded sentences using chosen method

