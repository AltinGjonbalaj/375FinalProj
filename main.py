import pprint
import sys
import random
from numpy import inf
import heapq

# Printer formatting
pp = pprint.PrettyPrinter(width=41)

# Function to find a minumum spanning tree using Prim's Algorith
def prim(graph):
	# distance, original index, parent
	keys = [[inf, x, -1] for x in range(len(graph))]
	keys[0][0] = 0
	min_queue = keys
	total_weight = 0

	MST = []

	while min_queue:
		heapq.heapify(min_queue)
		min_vert, node, parent = heapq.heappop(min_queue)
		MST.append( (node,parent) )
		total_weight += min_vert
		for index, each in enumerate(min_queue):
			weight = each[0]
			orig_index = each[1]
			parents = each[2]
			if graph[node][orig_index] < weight and graph[node][orig_index] != -1:
				min_queue[index][0] = graph[node][orig_index]
				min_queue[index][2] = node





	print(total_weight)
	print(MST)
	return MST


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
