from matplotlib import pyplot as plt


ages_x = list(range(25, 36)) 	#x-axis elements
others_y = [15000, 18000, 19500, 21000, 23500, 28300, 31400, 34560, 39560, 42000, 48000]	#y-axis element
python_y = [i+10000 for i in others_y]

plt.xkcd()
#plot(function takes color, linestyle, marker params)
plt.plot(ages_x, others_y, color='b', linestyle='--', marker='o', label='others')	#adding legends
plt.plot(ages_x, python_y, color='#ed2d2d', marker='.', label='python')	#adding legends

plt.xlabel('ages')
plt.ylabel('salaries')

plt.title('-:salaries comparision in Rupees:-')
plt.grid(True)

plt.legend()	#adding legends to the graph
plt.savefig('myfirst.jpg')
plt.show()
