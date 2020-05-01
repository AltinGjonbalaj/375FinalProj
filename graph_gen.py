import matplotlib # Graphing library
import pprint # For debugging
matplotlib.use('Agg') # Non-interactive, over ssh
import matplotlib.pyplot as plt # More graphing
import sys # for parsing arguments
pp = pprint.PrettyPrinter(width=41) # For debugging
import statistics # For mean
import math # log
import main # parses input

# Trim off outliers by percent
def trimmed(numbers, percent):
  num_to_trim = int(math.floor(percent * len(numbers))) # Where our cutoff is
  numbers.sort() # In order
  nums = numbers[num_to_trim:len(numbers)-num_to_trim] # actual cut off
  return nums

def stats_wrapper(numbers): # This is useful for log(x) b/c defined on range [1,inf]
    if(len(numbers) == 0):
        return 0
    else:
        return statistics.mean(numbers) # take mean

GRAPH_TYPE = "" # blank

# For how we graph
if sys.argv[1] == "random_input.txt":
    GRAPH_TYPE = "DENSE"
elif sys.argv[1] == "sparse_input.txt":
    GRAPH_TYPE = "SPARSE"
else:
    GRAPH_TYPE = "UNREC"


# pp.pprint(main.results)
if GRAPH_TYPE == "SPARSE":
    plt.suptitle("Prim's Algorith Runtime on sparse tree")
else:
    plt.suptitle("Prim's Algorith Runtime on dense tree")

plt.title("Sample size = {}".format(len(main.results)))


# X axis should be number of vertcs
to_iter = max([each['num_nodes'] for each in main.results]) # Where do we iterate up to
x = [x for x in range(0, to_iter + 1)] # actual X axis

# Y axis should be runtime

average_runtime_by_edge_count = [[] for each in range(max(x) + 1)]  # name is self descriptive
for each in main.results:
    index = each['num_nodes']
    average_runtime_by_edge_count[index].append(each['run_time'])

average_runtime_by_edge_count = map(lambda x: stats_wrapper(x), average_runtime_by_edge_count) # reduce it to averages



y = [runtime * 100 for runtime in average_runtime_by_edge_count] # Y axis values


# Baseline comparison
if GRAPH_TYPE == "SPARSE":
    # v lg(v)
    y_1 = [0]

    for V in range(1, to_iter + 1):
        val = (V) * math.log(V)
        y_1.append(val / 100000)

    line, = plt.plot(x, y_1, linestyle="dashed", color="green")
    line.set_label('|V| * log(|v|)')
    plt.legend()
elif GRAPH_TYPE == "DENSE":
    # v^2 lg(v)
    y_1 = [0]

    for V in range(1, to_iter + 1):
        val = (V ** 2) * math.log(V)
        y_1.append(val / 100000)

    line, = plt.plot(x, y_1, linestyle="dashed", color="green")
    line.set_label('|V|^2 * log(|v|)')
    plt.legend()


plt.scatter(x, y)
plt.draw()

plt.xlim(0, max(x))
plt.ylim(0, max(trimmed(y, 0.1)))

plt.xlabel("Verticies in Graph")
plt.ylabel("Runtime in milliseconds")

if GRAPH_TYPE == "SPARSE":
    filename = "sparse_runtime.png"
elif GRAPH_TYPE == "DENSE":
    filename = "dense_runtime.png"
else:
    filename = "random_input_runtime.png"
plt.savefig(filename)
