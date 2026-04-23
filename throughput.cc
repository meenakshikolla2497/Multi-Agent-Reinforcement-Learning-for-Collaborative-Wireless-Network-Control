import matplotlib.pyplot as plt

nodes = []
throughput = []

with open("results.txt", "r") as f:
    for line in f:
        data = line.split()
        nodes.append(int(data[0]))
        throughput.append(float(data[1]))

plt.plot(nodes, throughput, marker='o')
plt.title("Throughput vs Nodes")
plt.xlabel("Nodes")
plt.ylabel("Throughput (Kbps)")
plt.grid()
plt.savefig("throughput.png")
plt.show()
