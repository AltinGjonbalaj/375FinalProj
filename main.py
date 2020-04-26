import sys, getopt
def prim(line):
	pass
#will take in the 2d array, and print to a set output file 




def krus(line):
	pass



def main(argv):
	inputFile = ''
	outputFile = ''
	try:
      		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	for opt, arg in opts:
		if opt == '-i':
			inputFile = arg
		if opt == '-o':
			outputFile = arg
	readFile = open(inputFile)
	for line in readFile:
		line = line.split("|")
		#we need to parse line into 2d array // a matrix	
		prim(line)
		krus(line)
	readFile.close

