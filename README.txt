README.txt


# IMPORTANT: please bare in mind that the code won't run properly without the datasets
# which are too large to include in the submission. It was deemed sufficient to only submit
# the code files here.


This file describes the content of this folder, and the required libraries/modules.
This code was not designed as a single piece of software, but rather lots of individual
scripts which were used for certain tasks during the research project. They have to be
executed in a specific order to ensure the files are created at the right time for use
elsewhere. Please see the separate README.txt files in the subfolders for more information
on how to execute the individual parts, assuming the datasets are available.


All of the code contained here was developed using Python (version 2.7.10).

The following libraries/modules were used and are therefore required:
SciPy           (version 0.13.0.b1) http://scipy.org/
NumPy           (version 1.8.0rc1)  http://www.numpy.org/
NLTK            (version 3.0.2)     http://www.nltk.org/
scikit-learn    (version 0.16.1)    http://scikit-learn.org/stable/
NetworkX        (version 1.9.1)     https://networkx.github.io/


The directory structure should be as follows:
/code
    README.txt
    /classinet
        README.txt
        /helper-scripts
        /lib
    	/output-700
    	    /agreement-data
            /classifiers
            /expanded-data
            /rbf-predictions
            /svm-predictions
    	    /target-train-data
    /evaluation
        README.txt

where, /classinet contains all code pertaining to ClassiNet methods, /lib contains
some files with commonly used methods, /helper-scripts contains the Python scripts that
are not essential, but were used for specific tasks, /output-700 is where the various
output will go (as an example), and /evaluation contains the code for the SCL and FTS
implementations used for comparison, and the sentiment classifier code.

