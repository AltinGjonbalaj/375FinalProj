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
	print 'Input is ', inputFile
	print 'Output is ', outputFile
}
