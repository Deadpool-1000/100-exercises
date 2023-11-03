import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://pythonhow.com/media/data/sampledata.txt')
plt.plot(data)
plt.show()