import matplotlib
import pprint
matplotlib.use('Agg') # Non-interactive, over ssh
import matplotlib.pyplot as plt
import sys
pp = pprint.PrettyPrinter(width=41)
import statistics
import math
import main

# Trim off outliers by percent
def trimmed(numbers, percent):
  num_to_trim = int(math.floor(percent * len(numbers)))
  numbers.sort()
  nums = numbers[num_to_trim:len(numbers)-num_to_trim]
  return nums

def stats_wrapper(numbers):
    if(len(numbers) == 0):
        return 0
    else:
        return statistics.mean(numbers)

GRAPH_TYPE = ""

if sys.argv[1] == "random_input.txt":
    GRAPH_TYPE = "DENSE"
elif sys.argv[1] == "sparse_input.txt":
    GRAPH_TYPE = "SPARSE"


# pp.pprint(main.results)
if GRAPH_TYPE == "SPARSE":
    plt.suptitle("Prim's Algorith Runtime on sparse tree")
else:
    plt.suptitle("Prim's Algorith Runtime on dense tree")

plt.title("Sample size = {}".format(len(main.results)))


# X axis should be number of vertcs
to_iter = max([each['num_nodes'] for each in main.results])
x = [x for x in range(0, to_iter + 1)]

# Y axis should be runtime

average_runtime_by_edge_count = [[] for each in range(max(x) + 1)]
for each in main.results:
    index = each['num_nodes']
    average_runtime_by_edge_count[index].append(each['run_time'])

average_runtime_by_edge_count = map(lambda x: stats_wrapper(x), average_runtime_by_edge_count)



y = [runtime * 100 for runtime in average_runtime_by_edge_count]


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
else:
    filename = "dense_runtime.png"
plt.savefig(filename)
