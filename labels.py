from matplotlib import pyplot as plt 

ages_x = list(range(25, 36)) 	#x-axis elements
others_y = [15000, 18000, 19500, 21000, 23500, 28300, 31400, 34560, 39560, 42000, 48000]	#y-axis element

plt.plot(ages_x, others_y)

#add labels
plt.xlabel('ages')
plt.ylabel('salaries')

plt.show()