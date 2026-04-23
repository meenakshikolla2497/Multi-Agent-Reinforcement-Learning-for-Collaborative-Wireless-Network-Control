import matplotlib.pyplot as plt

nodes = []
pdr = []

with open("results.txt", "r") as f:
    for line in f:
        data = line.split()
        nodes.append(int(data[0]))
        pdr.append(float(data[2]))

plt.plot(nodes, pdr, marker='s')
plt.title("PDR vs Nodes")
plt.xlabel("Nodes")
plt.ylabel("PDR (%)")
plt.grid()
plt.savefig("pdr.png")
plt.show()
