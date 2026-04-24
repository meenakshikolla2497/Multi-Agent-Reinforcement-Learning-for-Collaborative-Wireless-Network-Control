#include <iostream>
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/mobility-module.h"
#include "ns3/wifi-module.h"
#include "ns3/internet-module.h"
#include "ns3/applications-module.h"
#include "ns3/flow-monitor-module.h"

using namespace ns3;

int main ()
{
    std::cout << "Simulation started" << std::endl;

    // 🔹 Change this value for experiments: 5, 10, 15, 20
    uint32_t numNodes = 10;

    NodeContainer nodes;
    nodes.Create(numNodes);

    // 🔹 WiFi configuration
    WifiHelper wifi;
    wifi.SetStandard(WIFI_STANDARD_80211g);

    YansWifiPhyHelper phy;
    YansWifiChannelHelper channel = YansWifiChannelHelper::Default();
    phy.SetChannel(channel.Create());

    WifiMacHelper mac;
    mac.SetType("ns3::AdhocWifiMac");

    NetDeviceContainer devices = wifi.Install(phy, mac, nodes);

    // 🔹 Mobility model
    MobilityHelper mobility;
    mobility.SetMobilityModel("ns3::RandomWalk2dMobilityModel",
                              "Bounds", RectangleValue(Rectangle(-50, 50, -50, 50)));
    mobility.Install(nodes);

    // 🔹 Internet stack
    InternetStackHelper stack;
    stack.Install(nodes);

    // 🔹 IP addressing (IMPORTANT: assign only once)
    Ipv4AddressHelper address;
    address.SetBase("10.1.1.0", "255.255.255.0");
    Ipv4InterfaceContainer interfaces = address.Assign(devices);

    // 🔹 Applications
    uint16_t port = 9;

    // Server on node 1
    UdpServerHelper server(port);
    ApplicationContainer serverApp = server.Install(nodes.Get(1));
    serverApp.Start(Seconds(1.0));
    serverApp.Stop(Seconds(10.0));

    // Client on node 0
    UdpClientHelper client(interfaces.GetAddress(1), port);
    client.SetAttribute("MaxPackets", UintegerValue(100));
    client.SetAttribute("Interval", TimeValue(Seconds(0.1)));
    client.SetAttribute("PacketSize", UintegerValue(1024));

    ApplicationContainer clientApp = client.Install(nodes.Get(0));
    clientApp.Start(Seconds(2.0));
    clientApp.Stop(Seconds(10.0));

    // 🔹 Flow Monitor
    FlowMonitorHelper flowmon;
    Ptr<FlowMonitor> monitor = flowmon.InstallAll();

    Simulator::Stop(Seconds(10.0));
    Simulator::Run();

    monitor->CheckForLostPackets();

    std::map<FlowId, FlowMonitor::FlowStats> stats = monitor->GetFlowStats();

    for (auto &flow : stats)
    {
        std::cout << "Flow ID: " << flow.first << std::endl;
        std::cout << "Tx Packets: " << flow.second.txPackets << std::endl;
        std::cout << "Rx Packets: " << flow.second.rxPackets << std::endl;

        if (flow.second.rxPackets > 0)
        {
            double timeDuration =
                flow.second.timeLastRxPacket.GetSeconds() -
                flow.second.timeFirstTxPacket.GetSeconds();

            double throughput =
                (flow.second.rxBytes * 8.0) / (timeDuration * 1024);

            std::cout << "Throughput: " << throughput << " Kbps" << std::endl;
        }
    }

    std::cout << "Simulation finished" << std::endl;

    Simulator::Destroy();
    return 0;
}
