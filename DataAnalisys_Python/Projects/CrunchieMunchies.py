'''
1.First, import numpy.
2.Look over the cereal.csv file. This file contains the reported calorie amounts for different cereal brands. Load the data from the file and save it as calorie_stats.
To learn more about reading data from a CSV using NumPy, read this documentation page.
3.There are 60 calories per serving of CrunchieMunchies. How much higher is the average calorie count of your competition?
Save the answer to the variable average_calories and print the variable to the terminal to see the answer.
4.Does the average calorie count adequately reflect the distribution of the dataset? Let’s sort the data and see.
Sort the data and save the result to the variable calorie_stats_sorted. Print the sorted data to the terminal.
5.Do you see what I’m seeing? Looks like the majority of the cereals are higher than the mean. Let’s see if the median is a better representative of the dataset.
Calculate the median of the dataset and save your answer to median_calories. Print the median so you can see how it compares to the mean.
6.While the median demonstrates that at least half of our values are over 100 calories, it would be more impressive to show that a significant portion of the competition has a higher calorie count that CrunchieMunchies.
Calculate different percentiles and print them to the terminal until you find the lowest percentile that is greater than 60 calories. Save this value to the variable nth_percentile.
7.While the percentile shows us that the majority of the competition has a much higher calorie count, it’s an awkward concept to use in marketing materials.
Instead, let’s calculate the percentage of cereals that have more than 60 calories per serving. Save your answer to the variable more_calories and print it to the terminal.
8.Wow! That’s a really high percentage. That’s going to be very useful when we promote CrunchieMunchies. But one question is, how much variation exists in the dataset? Can we make the generalization that most cereals have around 100 calories or is the spread even greater?
Calculate the amount of variation by finding the standard deviation. Save your answer to calorie_std and print to the terminal. How can we incorporate this value into our analysis?
9.Write a short paragraph that sums up your findings and how you think this data could be used to Yummy Corp’s advantage when marketing CrunchieMunchies.
'''
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

nth_percentile = np.percentile(calorie_stats, 60)
print(nth_percentile)

more_calories = np.mean(calorie_stats > 60) #Devuelve el porcentaje de cereales que tiene mas de 60 calorias
print(more_calories)

calorie_std = np.std(calorie_stats)
print(calorie_std)