import matplotlib.pyplot as plt

nodes = []
delay = []

with open("results.txt", "r") as f:
    for line in f:
        data = line.split()
        nodes.append(int(data[0]))
        delay.append(float(data[4]))

plt.plot(nodes, delay, marker='o')
plt.title("Delay vs Nodes")
plt.xlabel("Nodes")
plt.ylabel("Delay (sec)")
plt.grid()
plt.savefig("delay.png")
plt.show()
