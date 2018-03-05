import lib.utility as u
merge_file1 = 'output-700/expanded-data/new-test-all-neighb_linear_svm.txt'
merge_file2 = 'output-700/expanded-data/new-test-all-neighb_rbf_svm.txt'
    
    # Write new, expanded data to file
    with open(c.expanded_data_dir + output_file, "w") as file:
        for s in sentences:
            for i in s:
                file.write(i + " ")
            file.write("\n")
