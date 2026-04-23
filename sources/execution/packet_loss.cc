import matplotlib.pyplot as plt

nodes = []
packet_loss = []

with open("results.txt", "r") as f:
    for line in f:
        data = line.split()
        nodes.append(int(data[0]))
        packet_loss.append(float(data[3]))

plt.plot(nodes, packet_loss, marker='^')
plt.title("Packet Loss vs Nodes")
plt.xlabel("Nodes")
plt.ylabel("Packet Loss")
plt.grid()
plt.savefig("packet_loss.png")
plt.show()
