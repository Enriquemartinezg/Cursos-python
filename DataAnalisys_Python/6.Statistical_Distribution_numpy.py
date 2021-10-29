'''This lesson will cover:
How to generate and graph histograms
How to identify different distributions by their shape
Normal distributions
How standard deviations relate to normal distributions
Binomial distributions'''

# HISTOGRAMAS
import numpy as np
# Write matplotlib import here:
from matplotlib import pyplot as plt
commutes = np.genfromtxt('commutes.csv', delimiter=',')

# Plot histogram here:
plt.hist(commutes, range=(20, 51), bins=6) #range (rango de muestra del grafico)/bins(conjunto de datos representados por una unica barra)
plt.show()

#-----------------
import numpy as np
from matplotlib import pyplot as plt

# Brachiosaurus
b_data = np.random.normal(6.7, 0.7, size=1000) #genera una distribución normal de 1000 casos con media 6.7 y desviación estándar 0.7

# Fictionosaurus
f_data = np.random.normal(7.7, 0.3, size=1000)

plt.hist(b_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Brachiosaurus')
plt.hist(f_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()

mystery_dino = "brachiosaurus"
answer = False

'''As we saw in the previous exercise, no matter what mean and standard deviation we choose, 68% of our samples will fall between +/- 1 standard deviation of the mean!

In fact, here are a few more helpful rules for normal distributions:

68% of our samples will fall between +/- 1 standard deviation of the mean
95% of our samples will fall between +/- 2 standard deviations of the mean
99.7% of our samples will fall between +/- 3 standard deviations of the mean'''

#----------
#500 emails con un 5% prob de que abran el email y donen. 10000 pruebas
'a = np.random.binomial(N, P, size)'
emails = np.random.binomial(500, 0.05, size=10000)
plt.hist(emails, normed=True)
plt.show()

'''It takes the following arguments:

N: The number of samples or trials
P: The probability of success
size: The number of experiments'''

#Remember that taking the mean of a logical statement will give us the percent of values that satisfy our logical statement.

no_emails = np.mean(emails == 0) #probabilidad de que no abran ningun email
b_test_emails = np.mean(emails==40) #probabilidad de que  abran 40 emails
print(no_emails)
print(b_test_emails)

#--------------
sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# Calculate sunflowers_normal here:
sunflowers_normal = np.random.normal(
  loc=sunflowers_mean,
  scale=sunflowers_std,
  size=5000
)

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='Observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='Normal', normed=True)
plt.legend()
plt.show()


# Calculate probabilities here:
experiments = np.random.binomial(200, 0.1, size=5000)
prob = np.mean(experiments < 20)
print(prob)