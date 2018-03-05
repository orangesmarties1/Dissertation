# To compute stat significance with binomial test using SciPy.


import scipy.stats as s


if __name__ == "__main__":
    b = 0.7631
    # N=num_correct, S=sample_size, b=baseline_accuracy
    p_val = s.binom_test(N, S, b)
