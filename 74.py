import pandas

data1 = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data2 = pandas.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")
data = pandas.concat([data1, data2])
data.to_csv('out74.txt', index=None)