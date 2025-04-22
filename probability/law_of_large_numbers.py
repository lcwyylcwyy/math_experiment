import numpy as np
import matplotlib.pyplot as plt

# Binomial Law of Large Numbers 
def binomial_law_of_large_numbers(num, p, n, num_trials):
    """
    Simulate the Binomial Law of Large Numbers.
    
    Parameters:
    num (int): Number of successes in each trial.
    p (float): Probability of success in each trial.
    n (int): Number of trials in each experiment.
    num_trials (int): Number of experiments to simulate.
    
    Returns:
    list: List of sample means from each experiment.
    """
        # Simulate n trials with success probability p
    trials = np.random.binomial(num, p, size=[num_trials, n])
    
    return trials

p = 0.7
number_exp = 1
n_array = [10, 30, 90, 270, 810 ]
trails_number = 100
epislon = 0.05

for n in n_array:
    trails = binomial_law_of_large_numbers(number_exp, p, n, trails_number)
    xr = trails.sum(axis=1) / n - p
    count = np.sum(abs(xr) <= epislon)
    fre = 1 - count / trails_number
    print(f"n={n}次实验， m={trails_number}组重复， xr 的频率的差异:", fre)
    print(f"n={n}次实验， m={trails_number}组重复， xr <= 0.05 的次数:", count)

# trails = binomial_law_of_large_numbers(number_exp, p, n, trails_number)
# xr = trails.sum(axis=1) / n - p



