import matplotlib
import pprint
matplotlib.use('Agg') # Non-interactive, over ssh
import matplotlib.pyplot as plt
pp = pprint.PrettyPrinter(width=41)

import main

# pp.pprint(main.results)

plt.suptitle("Prim's Algorith Runtime")
plt.title("Number of graphs = {}".format(len(main.results)))


# X axis should be number of edges
x = [each['edges_in_MST'] for each in main.results]

# Y axis should be runtime
y = [each['run_time'] * 100 for each in main.results]

# print(x)
# print(y)


plt.scatter(x, y)
plt.draw()

plt.xlim(0, max(x))
plt.ylim(0, max(y))

plt.xlabel("Edges in Graph")
plt.ylabel("Runtime 1/100th second")

filename = "runtime.png"
plt.savefig(filename)
