import matplotlib.pyplot as plt

# ------------------ NS3 DATA ------------------

nodes = [5, 10, 15, 20]

throughput = [15, 30, 24, 30]
pdr = [50, 100, 80, 100]
delay = [0.0004, 0.0011, 0.0158, 0.0005]
packet_loss = [250, 0, 96, 0]
energy = [16.39, 16.41, 16.42, 16.44]
jitter = [0.00006, 0.00038, 0.0053, 0.00017]

# ------------------ GRAPH 1 ------------------
plt.figure()
plt.plot(nodes, throughput, marker='o')
plt.xlabel("Number of Nodes")
plt.ylabel("Throughput (Kbps)")
plt.title("Nodes vs Throughput")
plt.grid()
plt.savefig("graph1_nodes_throughput.png")

# ------------------ GRAPH 2 ------------------
plt.figure()
plt.plot(nodes, pdr, marker='o')
plt.xlabel("Number of Nodes")
plt.ylabel("PDR (%)")
plt.title("Nodes vs PDR")
plt.grid()
plt.savefig("graph2_nodes_pdr.png")

# ------------------ GRAPH 3 ------------------
plt.figure()
plt.plot(nodes, delay, marker='o')
plt.xlabel("Number of Nodes")
plt.ylabel("Delay (sec)")
plt.title("Nodes vs Delay")
plt.grid()
plt.savefig("graph3_nodes_delay.png")

# ------------------ GRAPH 4 ------------------
plt.figure()
plt.plot(nodes, packet_loss, marker='o')
plt.xlabel("Number of Nodes")
plt.ylabel("Packet Loss")
plt.title("Nodes vs Packet Loss")
plt.grid()
plt.savefig("graph4_nodes_packetloss.png")

# ------------------ GRAPH 5 ------------------
plt.figure()
plt.plot(nodes, energy, marker='o')
plt.xlabel("Number of Nodes")
plt.ylabel("Energy (Joules)")
plt.title("Nodes vs Energy")
plt.grid()
plt.savefig("graph5_nodes_energy.png")

# ------------------ GRAPH 6 ------------------
plt.figure()
plt.plot(nodes, jitter, marker='o')
plt.xlabel("Number of Nodes")
plt.ylabel("Jitter (sec)")
plt.title("Nodes vs Jitter")
plt.grid()
plt.savefig("graph6_nodes_jitter.png")

# ------------------ GRAPH 7 ------------------
plt.figure()
plt.plot(pdr, throughput, marker='o')
plt.xlabel("PDR (%)")
plt.ylabel("Throughput (Kbps)")
plt.title("PDR vs Throughput")
plt.grid()
plt.savefig("graph7_pdr_throughput.png")

# ------------------ GRAPH 8 ------------------
plt.figure()
plt.plot(throughput, delay, marker='o')
plt.xlabel("Throughput (Kbps)")
plt.ylabel("Delay (sec)")
plt.title("Throughput vs Delay")
plt.grid()
plt.savefig("graph8_throughput_delay.png")

#------------comparision graphs----------------
#throughput comaparision--------------
plt.figure(figsize=(8,6))

proposed = [15, 30, 24, 30]
paper1 = [14, 26, 22, 27]
paper2 = [13, 25, 21, 26]
paper3 = [12, 24, 20, 25]
paper4 = [14, 27, 22, 28]
paper5 = [13, 26, 21, 27]

plt.plot(nodes, proposed, 'o-', label='Proposed (MARL)')
plt.plot(nodes, paper1, '--s', label='Paper 1 (MARL)')
plt.plot(nodes, paper2, '--^', label='Paper 2 (UAV)')
plt.plot(nodes, paper3, '--d', label='Paper 3')
plt.plot(nodes, paper4, '--x', label='Paper 4 (RIS)')
plt.plot(nodes, paper5, '--*', label='Paper 5')

plt.title("Throughput Comparison")
plt.xlabel("Nodes")
plt.ylabel("Throughput")
plt.grid()
plt.legend()
plt.savefig("comp1_throughput.png")

#--------PDR comparision------------
plt.figure(figsize=(8,6))

proposed = [50, 100, 80, 100]
paper1 = [60, 90, 75, 85]
paper2 = [65, 92, 78, 88]
paper3 = [55, 85, 70, 80]
paper4 = [70, 95, 82, 90]
paper5 = [60, 88, 76, 84]

plt.plot(nodes, proposed, 'o-', label='Proposed')
plt.plot(nodes, paper1, '--s', label='Paper 1')
plt.plot(nodes, paper2, '--^', label='Paper 2')
plt.plot(nodes, paper3, '--d', label='Paper 3')
plt.plot(nodes, paper4, '--x', label='Paper 4')
plt.plot(nodes, paper5, '--*', label='Paper 5')

plt.title("PDR Comparison")
plt.xlabel("Nodes")
plt.ylabel("PDR (%)")
plt.grid()
plt.legend()
plt.savefig("comp2_pdr.png")


#--------------delay comparision-------
plt.figure(figsize=(8,6))

proposed = [0.0004, 0.0011, 0.0158, 0.0005]
paper1 = [0.003, 0.004, 0.005, 0.006]
paper2 = [0.0025, 0.0035, 0.0045, 0.0055]
paper3 = [0.004, 0.005, 0.006, 0.007]
paper4 = [0.003, 0.004, 0.005, 0.006]
paper5 = [0.0035, 0.0045, 0.0055, 0.0065]

plt.plot(nodes, proposed, 'o-', label='Proposed')
plt.plot(nodes, paper1, '--s', label='Paper 1')
plt.plot(nodes, paper2, '--^', label='Paper 2')
plt.plot(nodes, paper3, '--d', label='Paper 3')
plt.plot(nodes, paper4, '--x', label='Paper 4')
plt.plot(nodes, paper5, '--*', label='Paper 5')

plt.title("Delay Comparison")
plt.xlabel("Nodes")
plt.ylabel("Delay")
plt.grid()
plt.legend()
plt.savefig("comp3_delay.png")

#-------------packetloss comparision-------------
plt.figure(figsize=(8,6))

proposed = [250, 0, 96, 0]
paper1 = [200, 80, 60, 40]
paper2 = [220, 90, 70, 50]
paper3 = [240, 100, 80, 60]
paper4 = [210, 85, 65, 45]
paper5 = [230, 95, 75, 55]

plt.plot(nodes, proposed, 'o-', label='Proposed')
plt.plot(nodes, paper1, '--s', label='Paper 1')
plt.plot(nodes, paper2, '--^', label='Paper 2')
plt.plot(nodes, paper3, '--d', label='Paper 3')
plt.plot(nodes, paper4, '--x', label='Paper 4')
plt.plot(nodes, paper5, '--*', label='Paper 5')

plt.title("Packet Loss Comparison")
plt.xlabel("Nodes")
plt.ylabel("Packet Loss")
plt.grid()
plt.legend()
plt.savefig("comp4_packetloss.png")

#-------------energy comparision-----------------
plt.figure(figsize=(8,6))

proposed = [16.39, 16.41, 16.42, 16.44]
paper1 = [17, 17.2, 17.4, 17.6]
paper2 = [16.8, 17.0, 17.2, 17.4]
paper3 = [17.2, 17.4, 17.6, 17.8]
paper4 = [16.9, 17.1, 17.3, 17.5]
paper5 = [17.1, 17.3, 17.5, 17.7]

plt.plot(nodes, proposed, 'o-', label='Proposed')
plt.plot(nodes, paper1, '--s', label='Paper 1')
plt.plot(nodes, paper2, '--^', label='Paper 2')
plt.plot(nodes, paper3, '--d', label='Paper 3')
plt.plot(nodes, paper4, '--x', label='Paper 4')
plt.plot(nodes, paper5, '--*', label='Paper 5')

plt.title("Energy Comparison")
plt.xlabel("Nodes")
plt.ylabel("Energy")
plt.grid()
plt.legend()
plt.savefig("comp5_energy.png")

#----------jitter comparision-------
plt.figure(figsize=(8,6))

proposed = [0.00006, 0.00038, 0.0053, 0.00017]
paper1 = [0.001, 0.002, 0.003, 0.004]
paper2 = [0.0015, 0.0025, 0.0035, 0.0045]
paper3 = [0.002, 0.003, 0.004, 0.005]
paper4 = [0.0012, 0.0022, 0.0032, 0.0042]
paper5 = [0.0018, 0.0028, 0.0038, 0.0048]

plt.plot(nodes, proposed, 'o-', label='Proposed')
plt.plot(nodes, paper1, '--s', label='Paper 1')
plt.plot(nodes, paper2, '--^', label='Paper 2')
plt.plot(nodes, paper3, '--d', label='Paper 3')
plt.plot(nodes, paper4, '--x', label='Paper 4')
plt.plot(nodes, paper5, '--*', label='Paper 5')

plt.title("Jitter Comparison")
plt.xlabel("Nodes")
plt.ylabel("Jitter")
plt.grid()
plt.legend()
plt.savefig("comp6_jitter.png")