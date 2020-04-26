import sys, getopt

def main(argv){
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
		#we need to parse line into 2d array // a matrix	
		prim(line)
		kruskals(line)
	readFile.close
}
