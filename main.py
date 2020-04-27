import pprint
import sys
import random
from numpy import inf
import heapq


pp = pprint.PrettyPrinter(width=41)

def prim(graph):
	included_nodes = set()
	key = set() # visitable
	root_node_index = random.choice(range(len(graph))) # Arbitrarily decide where we start iterating






def krus(graph):
	pass



def main():
	inputFile = 'input.txt'
	outputFile = 'output.txt'

	with open(inputFile) as read_file:
		for line in read_file.read().strip().split("\n"):
			rows = line.split("|")
			graph = [[-1 for x in range(len(rows))] for x in range(len(rows))] # initalize n x n matrix w/ -1s
			for index, each in enumerate(rows):
				graph[index] = map(lambda x: int(x), each.split(",")) # break the line into individual strings, then map to ints
			# pp.pprint(graph)
			prim_result = prim(graph)

main()
