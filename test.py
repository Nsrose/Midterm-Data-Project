import csv
gdpDict = {}
with open('gdp data.csv', 'rb') as csvfile: 
	dataReader = csv.reader(csvfile, delimiter=',')
	for row in dataReader:
		state = row[0]
		row.pop(0)
		gdpDict[state] = float(row[0])


gdpDict.sort(key=lambda x: x[0], reverse= False)
print gdpDict

