
#region imports
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
#endregion


def plot_probability_density(mean, std_dev, condition_value):
    '''Calculate the probability P(x < 1 | N(0, 1))
    this function takes arguments mean, standard deviation, and a condition value'''
    x = np.linspace(-5, 5, 1000)                        # makes values for x
    pdf = stats.norm.pdf(x, mean, std_dev)              # probability density function
    cdf = stats.norm.cdf(x, mean, std_dev)              # cumulative distribution function
    probability = 1 - stats.norm.cdf(condition_value, mean, std_dev)  # calculate the probability P(x > μ + 2σ | N(175, 3))

    plt.figure(figsize=(10, 6))             # set up the plot 

    plt.subplot(2, 1, 1)                                           #plot setup from chatgpt
    plt.plot(x, pdf, label='Probability Density Function')
    plt.fill_between(x, pdf, where=(x < 1), color='blue', alpha=0.5)
    plt.title('Probability Density Function')
    plt.xlabel('x')
    plt.ylabel('Probability')

    plt.subplot(2, 1, 2)
    plt.plot(x, cdf, label='Cumulative Distribution Function')
    plt.fill_between(x, cdf, where=(x < 1), color='magenta', alpha=0.5)
    plt.axvline(x=1, color='red', linestyle='--')
    plt.title('Cumulative Distribution Function')
    plt.xlabel('x')
    plt.ylabel('Probability')

    plt.show()

    # Print the probability P(x > μ + 2σ | N(175, 3))
    print("Probability (x > μ + 2σ | N(175, 3)):", probability)

mean = 0
std_dev = 1
condition_value = 175

plot_probability_density(mean, std_dev, condition_value)