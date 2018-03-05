import target_predictor as t
from sklearn import svm
import lib.utility as u
import config as c

# Trains all classifiers and stores them here in a dictionary
def store_classifier(word, classifiers):
	if word not in classifiers:
		print 'starting storage method for', word
		clf = t.get_classifier(word)
		classifiers[word] = clf
		for key in classifiers:
		    print key 


if __name__ == '__main__':
	# Load feature space and target words
    features_index = u.read_features_file(c.output_dir + "feat-space.txt")
    feature_size = len(features_index) #5000 features
    target_words = u.get_target_words()
    target_count = 0
    classifiers = {}

    counter = 0
    for target in target_words:
    	counter += 1
    	print 'ok lets sort the classifier for', target
    	store_classifier(target, classifiers)

