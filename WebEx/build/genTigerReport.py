
import numpy as np
import random
from matplotlib import pyplot as plt


def calclim(data):
	try:
		if None == data :
			return None
		
		arrLim = []
		arrLim[0] = min(data)
		arrLim[1] = max(data) * 1.1
		
		return arrLim
	except Exception, e:
		print("calclim", e)
		return None


def drawBar(xData, yData, alpha = .5, color = 'g'):
	try:
		if None == yData :
			return False
		
		arrXlim = calclim(xData)
		arrYlim = calclim(yData)
		
		plt.xlim(arrXlim[0], arrXlim[1])
		plt.ylim(arrYLim[0], arrYLim[1])		
		
		plt.bar(x, data, alpha, color)
		plt.show()
		
		return True
	except Exception, e:
		print("drawBar", e)
		return False



'''
def drawHistograms(args) :
	try:
		
		data = np
		
		return True
	except Exception, e:
		print("drawHistograms", e)
		return False
'''


'''

data = [0.15, 0.25, 0.35, 0.45, 0.55] 
#np.random.normal(0, 20, 1000)
bins = [10, 20, 30, 40, 50]
#np.arange(-100, 100, 5)

print('data:', data)
print('bins:', bins)

#plt.xlim([min(data)-5, max(data)+5])
plt.xlim(0, 10)
plt.ylim(0, 1)



plt.hist(data, bins=bins, alpha=0.5)
plt.title('Random Gaussian data (fixed bin size)')
plt.xlabel('variable X (bin size = 5)')
plt.ylabel('count')
'''

#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib as mpl

#mpl.rcParams['font.family'] = 'sans-serif'
#mpl.rcParams['font.sans-serif'] = [u'SimHei']

y_data = [3, 4, 8, 6, 7]
x_data = [1, 2, 3, 4, 5]
drawBar(x_data, y_data)

