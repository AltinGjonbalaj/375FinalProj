import pprint
import sys
import random
from numpy import inf
import heapq

# Printer formatting
pp = pprint.PrettyPrinter(width=41)

# Function to find a minumum spanning tree using Prim's Algorith
def prim(graph):
	# -1 = nil, per slides
	keys = [[inf, x] for x in range(len(graph))]
	keys[0][0] = 0
	min_queue = keys

	MST = []

	while min_queue:
		heapq.heapify(min_queue)
		min_vert, node = heapq.heappop(min_queue)
		MST.append(node)
		for index, each in enumerate(min_queue):
			weight = each[0]
			orig_index = each[1]
			if graph[min_vert][orig_index] < weight and graph[min_vert][orig_index] != -1:
				min_queue[index][0] = graph[min_vert][orig_index]

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
