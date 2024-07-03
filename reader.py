import csv
from source import Source

def get_source(sources,source_file):
    
    with open(source_file,newline='') as csvfile:
        datareader = csv.reader(csvfile,delimiter=',',quotechar='|')
        for row in datareader:
            sources.append(Source(row[0],row[1],row[2],row[3]))