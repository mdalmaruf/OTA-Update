# [Faster Fog Computing based Over-the-air Vehicular Updates: A Transfer Learning Approach](https://ieeexplore.ieee.org/abstract/document/9496152) 

Authors:
Md Al Maruf, Anil Singh, Akramul Azim, Nitin Auluck
#### Journal: IEEE Transactions on Services Computing, 2021

## Abstract
> Fog computing is a promising option for time sensitive vehicular over-the-air (OTA) updates, as it can offer enhanced network durability and lower communication delays, versus the cloud. Fog node utilization is non-deterministic, largely owing to vehicular traffic patterns. The resultant over provisioning of resources manifests itself in increased communication and handover delays. Based on an analysis of regional traffic patterns, our proposed algorithm determines the optimal number of fog nodes required for OTA updates. The efficacy of our proposed approach is demonstrated using a case study that considers handover delay, propagation delay, transmission rate and vehicular mobility to predict the OTA update time. We employ a machine learning model for predicting the communication delay between fog devices and vehicles. Using European WiFi hotspot signal strength NYC dataset and 5G dataset, we observe that the proposed approach increases net reserve fog resources by 26.57% on average, and reduces the OTA update time by 5.34%. We test the scalability of our approach by analyzing the performance in terms of average throughput while varying the number of vehicles and OTA update size. The performance of the proposed OTA update scheme on simulations has been corroborated by implementation on a real-world testbed

## Full Paper: [Download](https://ieeexplore.ieee.org/abstract/document/9496152)

## Supplemental Materials: [Download](https://github.com/mdalmaruf/OTA-Update/blob/c480ca2d180b516a0f7261070bd52e4454c469dc/Faster%20Fog%20Computing%20OTA%20Update-Transfer%20Learning%20Approach%20(Supplemental%20Materials).pdf)

> Please find the supplemental materials over here. The file is uploades as pdf in this Repository. [PDF](https://github.com/mdalmaruf/OTA-Update/blob/c480ca2d180b516a0f7261070bd52e4454c469dc/Faster%20Fog%20Computing%20OTA%20Update-Transfer%20Learning%20Approach%20(Supplemental%20Materials).pdf)

## Simulation and Testbed Details

### Simulation
- Conducted using OTA update time through Mininet-WiFi.
- Components involved:
  - Handover delay
  - Propagation delay

### Testbed
- Fog nodes connected through network routers with varying WiFi ranges.
- Fog nodes and vehicles are implemented as Virtual Machines (VMs) using the QEMU virtualizer.
  - VMs run on separate laptops.
  - QEMU emulates the ARM hardware architecture.
- Integration of a pre-existing OTA update framework: [Uptane](https://uptane.github.io/).
- VM Setup:
  - Multiple VMs created, representing different fog nodes and vehicles/cars.
  - Each VM has 4GB RAM and runs Linux.
- Connection specifications:
  - Connection established through a 300Mbps N TPLink wireless router (TL-WR841N).
  - Utilizes TCP/IP for data transmission.
  - Maximum router coverage: approximately 70 meters.
- Fog Node Distribution:
  - Three fog nodes (1, 2, and 3) positioned 30 meters from the router.
  - Fog nodes are uniformly distributed in a cluster.
- Vehicles in the Cluster:
  - Eight (8) VMs represent vehicles.
