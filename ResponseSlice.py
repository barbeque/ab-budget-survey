import os
import csv
import StringIO

# cut a rectangle out of the data and return it as a csv blob
def extract(csvRows, columnsStart, columnsEnd, rowStart, rowEnd):
    trimmed_rows = csvRows[rowStart:(rowEnd+1)]
    result = []
    for row in trimmed_rows:
        result.append(row[columnsStart:(columnsEnd+1)])
    return result
    
def loadCsv(path):
    with open(path, 'r') as csvFile:
        csv_text = csvFile.read()
    reader = csv.reader(csv_text.split('\n'))
    result = []
    columns_count = 0
    for row in reader:
        if len(row) > 0:
            result.append(row)
            columns_count = max(columns_count, len(row))
    print 'ingested', len(result), 'rows x', columns_count, 'columns'
    return result
    
def writeCsv(csvRows, path):
    columns_count = 0
    with open(path, 'w') as outFile:
        for row in csvRows:
            outFile.write(','.join(row))
            outFile.write('\n')
            columns_count = max(columns_count, len(row))
    print 'wrote', len(csvRows), 'rows x', columns_count, 'columns to', path
        

def demo_sliceOutQuestion9():
    csvRows = loadCsv("Responses.csv")
    # columns P to X (index 15 to 23)
    # row start = 5th row (index 4)
    # row end = 40518th row (index 40517)
    extractedQuestionNine = extract(csvRows, 15, 23, 4, 40517)
    writeCsv(extractedQuestionNine, 'q9.csv')

if __name__ == '__main__': demo_sliceOutQuestion9()