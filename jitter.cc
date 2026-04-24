import matplotlib.pyplot as plt

nodes = []
jitter = []

with open("results.txt", "r") as f:
    for line in f:
        data = line.split()
        nodes.append(int(data[0]))
        jitter.append(float(data[6]))

plt.plot(nodes, jitter, marker='o')
plt.title("Jitter vs Nodes")
plt.xlabel("Nodes")
plt.ylabel("Jitter (sec)")
plt.grid()
plt.savefig("jitter.png")
plt.show()
