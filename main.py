import pprint
import sys
import random
from numpy import inf
import heapq
import time

# Printer formatting
pp = pprint.PrettyPrinter(width=41)

# Function to find a minumum spanning tree using Prim's Algorithm
# Function to find a minumum spanning tree using Prim's Algorith
# Key = an array of pairs of weight, index
# min_queue = a min queue for key, we use this to tell when prims is done
# total_weight = total weight of all the nodes
# MST = the solution set of vertices

def prim(graph):
	# distance, original index, parent
	keys = [[inf, x, -1] for x in range(len(graph))]
	keys[0][0] = 0
	min_queue = keys
	total_weight = 0

	MST = []

# loops through all nodes, removing one at a time until min queue is empty
# in each iteration you add the minimum vertice in min queue to the MST
# after adding min vert the for loop checks to see if you can update any of the weights in min queue
	while min_queue:
		heapq.heapify(min_queue)
		min_vert, node, parent = heapq.heappop(min_queue)
		MST.append( (node,parent) )
		total_weight += min_vert
		for index, each in enumerate(min_queue):
			weight = each[0]
			orig_index = each[1]
			parents = each[2]
			if graph[node][orig_index] != -1 and graph[node][orig_index] < weight:
				min_queue[index][0] = graph[node][orig_index]
				min_queue[index][2] = node
	return_obj = {
		"MST" : MST,
		"total_weight": total_weight,
		"num_nodes": len(graph),
		"edges_in_MST": len(MST) - 1, # substract 1 for the (0, -1) connection
	}
	# print(total_weight)
	# print(MST)
	return return_obj





# Results is a list, will hold dicts of result data
results = []


#parses input from our input file into a 2d array // matrix representation for a graph
# @DAVID WE SHOULD CALCULATE RUN TIME IN HERE AND PUSH IT TO A GRAPH BASED ON NUMBER OF NODES AND EDGES
def main():
	if len(sys.argv) != 2:
		print("Supply input file (input.txt)")
		exit(1)
	inputFile = sys.argv[1]
	outputFile = 'output.txt'



	# We could, theoretically add tons of error checking here, but we are generating the
	# inputing using a cpp program - we are only using trusted data...
	with open(inputFile) as read_file:
		for line in read_file.read().strip().split("\n"):
			rows = line.split("|")
			graph = [[-1 for x in range(len(rows))] for x in range(len(rows))] # initalize n x n matrix w/ -1s
			for index, each in enumerate(rows):
				# print("Parsing a line . . . ")
				try:
					graph[index] = map(lambda x: int(x), each.split(",")) # break the line into individual strings, then map to ints
				except Exception as e:
					print(e)
					print(line)
				# print("Parsed . . . ")


			start_time = time.time()
			# pp.pprint(graph)
			# print("Prim...")
			prim_result = prim(graph)
			end_time = time.time()
			run_time = end_time - start_time
			prim_result["run_time"] = run_time
			results.append(prim_result)

	if sys.argv[1] == "livetest.txt":
		pp.pprint(results)

	return results



main()
