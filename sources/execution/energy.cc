import matplotlib.pyplot as plt

nodes = []
energy = []

with open("results.txt", "r") as f:
    for line in f:
        data = line.split()
        nodes.append(int(data[0]))
        energy.append(float(data[5]))

plt.plot(nodes, energy, marker='o')
plt.title("Energy vs Nodes")
plt.xlabel("Nodes")
plt.ylabel("Energy (Joules)")
plt.grid()
plt.savefig("energy.png")
plt.show()
