# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:55:25 2020

@author: Maruf
"""
import car

import cluster
import network
import graphic
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#env = simpy.Environment()

#requirement mapping
#------------1=music
#------------2=brake
#------------3=security
#------------4=alert message

#car= car(id, cluster, long, lati, req, parent)

cluster1 =cluster.cluster(1)
cluster2 =cluster.cluster(2)
cluster3 =cluster.cluster(3)
cluster4 =cluster.cluster(4)
cluster5 =cluster.cluster(5)

#cluster1: red
car59 = car.Car(59, 1, 2, -77.0075055,	18.3267954,True)
car1 = car.Car(1,  1, 1, -89.65,	39.8, False)
car17 = car.Car(17, 1, 3, -62.2106241,	16.7909044, False)

car15 = car.Car(15, 1, 3, -75.8766333, -10.1968448, False)

#cluster2: blue
car2000 = car.Car(2000, 4, 4, -90.87153,	160.28268, True)
car1956 = car.Car(1956, 4, 3, -106.6633746,	124.7540279, False)
car1959 = car.Car(1959, 4, 3, -106.6633746,	124.7540279, False)

#cluster3: green
car107 = car.Car(107, 3, 3, -83.9055618,	89.7154835, True)
#car1 = car.Car(1, 3, 4, -71.9471867,	77.2154159, False)

car179 = car.Car(179, 3, 3, -103.9334354,	77.9005444, False)
car646 = car.Car(646, 4, 2, -48.4403573,	84.394682, False)

#cluster4: black
car2 = car.Car(2, 2, 3, -35.6040785,	-43.1155165, True)
car31 = car.Car(31, 2,  4, -41.8402054,	-12.5444681,False)
car47 = car.Car(47, 2, 2, -49.4262684,	-16.5030467, False)
car29 = car.Car(29, 2, 1, -30.1898025,	-9.2178609, False)
car60 = car.Car(60,  4, 4, -37.940316,	-70.539947, False)
car12 = car.Car(12,  1, 2, -20.04997,	-60.8943618, False)
#cluster5: magenta
car9 = car.Car(9, 4, 2, -88.4403573,	232.394682, True)
car24 = car.Car(24, 4, 1, -80.8172881,	270.1105068, False)
car16 = car.Car(16, 4, 2, -70.957345,	250.238934, False)


#car4 = car.Car(4, 1, 3, 16.1355432,	28.6488132,False)

#car6 = car.Car(6, 1, 2, -77.0075055,	18.3267954,True)
#car7 = car.Car(7, 3, 4, 34.0789969,	44.4309874,False)




#car13 = car.Car(13,  4, 3,79.4783816,	14.3059024, False)
#car14 = car.Car(14,  4, 1, 115.969683,	28.430921, False)

#car16 = car.Car(16, 4, 4, 171.0702405,	14.578621, False)

#car18 = car.Car(18, 2, 2, -49.4262684,	-16.5030467, False)
#car19 = car.Car(19, 3, 3, 53.9334354,	55.9005444, False)
#car20 = car.Car(20, 4, 2, -88.4403573,	232.394682, True)
#car21 = car.Car(21, 3, 2, 16.3106228,	57.9891702, False)
#car22 = car.Car(22, 3, 2, 10.7067713,	69.9162711, False)
#car23 = car.Car(23, 3, 1, 7.7342943,	54.5851876, False)
#car24 = car.Car(24, 4, 1, -80.8172881,	270.1105068, False)
#car25 = car.Car(25, 4, 2, -70.957345,	250.238934, False)
#car26 = car.Car(26, 4, 3, 112.805131,	21.956492, False)
#car27 = car.Car(27, 2, 1, 34.7395478,	-12.0663691, False)
#car28 = car.Car(28, 3, 1, 11.3353423,	46.2209242, False)

#car30 = car.Car(30, 3, 4, 44.5135399,	40.0534636, False)

net = network.network()

cluster1.cars.append(car59)
cluster1.cars.append(car1)
#cluster1.cars.append(car12)
cluster1.cars.append(car15)
cluster1.cars.append(car17)

cluster2.cars.append(car2)
cluster2.cars.append(car31)
cluster2.cars.append(car47)
cluster2.cars.append(car60)
cluster2.cars.append(car12)
#cluster2.cars.append(car27)
cluster2.cars.append(car29)


cluster3.cars.append(car107)
cluster3.cars.append(car179)
cluster3.cars.append(car646)
#cluster3.cars.append(car4)
#cluster3.cars.append(car7)
#cluster3.cars.append(car19)
#cluster3.cars.append(car21)
#cluster3.cars.append(car22)
#cluster3.cars.append(car23)
#cluster3.cars.append(car28)
#cluster3.cars.append(car30)


cluster4.cars.append(car2000)
cluster4.cars.append(car1956)
cluster4.cars.append(car1959)

#cluster4.cars.append(car13)
#cluster4.cars.append(car14)
#cluster4.cars.append(car16)


cluster5.cars.append(car9)
cluster5.cars.append(car24)
cluster5.cars.append(car16)
#cluster5.cars.append(car26)





net.clusters.append(cluster1)
net.clusters.append(cluster2)
net.clusters.append(cluster3)
net.clusters.append(cluster4)
net.clusters.append(cluster5)
print(len(net.clusters[0].cars))
print(len(net.clusters[1].cars))

#-----------------------graphics----------------------

for node in net.clusters[0].cars:
            #if(node.is_alive == True):
                #G.add_node(node.id,pos=(node.x,node.y))
        print(node.id)
                
                

G = nx.Graph()
fig, ax = plt.subplots(1,figsize=(7,5))
#G.add_node(0,pos=(self.mynetwork.xsize/2,self.mynetwork.xsize/2))
#for cl1 in self.cluster1
color_map = []
for node in net.clusters[0].cars:
    if(node.parent==True):
            node.is_CH=True
            G.add_node(node.id,pos=(node.x,node.y))
            color_map.append('YELLOW')
            art = mpatches.Circle((node.x,node.y),60.0, edgecolor='r',fill=False)
            ax.add_patch(art)
            break
print(node.id)
for node_next in net.clusters[0].cars:
    if(node_next.parent==False):
        G.add_node(node_next.id,pos=(node_next.x,node_next.y))
        G.add_edge(node_next.id,node.id)
        color_map.append('red')
        print(node_next.id)
 
for node2 in net.clusters[1].cars:
    if(node2.parent==True):
            node2.is_CH=True
            G.add_node(node2.id,pos=(node2.x,node2.y))
            color_map.append('YELLOW')
            art = mpatches.Circle((node2.x,node2.y),50.0, edgecolor='black',fill=False)
            ax.add_patch(art)
            break
print(node2.id)
       
for node_next in net.clusters[1].cars:
    if(node_next.parent==False):
        G.add_node(node_next.id,pos=(node_next.x,node_next.y))
        G.add_edge(node_next.id,node2.id)
        color_map.append('LIGHTGRAY')
        print(node_next.id) 
        
        
for node3 in net.clusters[2].cars:
    if(node3.parent==True):
            node3.is_CH=True
            G.add_node(node3.id,pos=(node3.x,node3.y))
            color_map.append('YELLOW')
            art = mpatches.Circle((node3.x,node3.y),40.0, edgecolor='green',fill=False)
            ax.add_patch(art)
            break
print(node3.id)
       
for node_next in net.clusters[2].cars:
    if(node_next.parent==False):
        G.add_node(node_next.id,pos=(node_next.x,node_next.y))
        G.add_edge(node_next.id,node3.id)
        color_map.append('green')
        print(node_next.id)           
        

for node4 in net.clusters[3].cars:
    if(node4.parent==True):
            node4.is_CH=True
            G.add_node(node4.id,pos=(node4.x,node4.y))
            color_map.append('YELLOW')
            art = mpatches.Circle((node4.x,node4.y),40.0, edgecolor='MEDIUMSLATEBLUE',fill=False)
            ax.add_patch(art)
            break
print(node4.id)
       
for node_next in net.clusters[3].cars:
    if(node_next.parent==False):
        G.add_node(node_next.id,pos=(node_next.x,node_next.y))
        G.add_edge(node_next.id,node4.id)
        color_map.append('MEDIUMSLATEBLUE')
        print(node_next.id)   
        
        
        
for node5 in net.clusters[4].cars:
    if(node5.parent==True):
            node5.is_CH=True
            G.add_node(node5.id,pos=(node5.x,node5.y))
            color_map.append('YELLOW')
            art = mpatches.Circle((node5.x,node5.y),40.0, edgecolor='magenta',fill=False)
            ax.add_patch(art)
            break
print(node5.id)
       
for node_next in net.clusters[4].cars:
    if(node_next.parent==False):
        G.add_node(node_next.id,pos=(node_next.x,node_next.y))
        G.add_edge(node_next.id,node5.id)
        color_map.append('magenta')
        print(node_next.id)         








      
nx.draw(G, nx.get_node_attributes(G, 'pos'), node_color=color_map, with_labels=True, node_size=800)
#ani = animation.FuncAnimation(fig, animate, interval=1000)
#plt.legend("Network")
# use parameter bbox_to_anchor to reposition
# the legend box outside the plot area
red_patch = mpatches.Patch(color='red', label='Cluster1, Size: 1615')
blue_patch = mpatches.Patch(color='MEDIUMSLATEBLUE', label='Cluster2, Size: 894')
green_patch = mpatches.Patch(color='green', label='Cluster3, Size: 674')
black_patch = mpatches.Patch(color='black', label='Cluster4, Size: 1949')
magenta_patch = mpatches.Patch(color='magenta', label='Cluster5, Size: 1228')
# plt.legend(handles=[red_patch])
# plt.legend(handles=[blue_patch])
plt.legend([red_patch,blue_patch,green_patch,black_patch, magenta_patch], ["Cluster1, Size: 1615 ", "Cluster2, Size: 894", "Cluster3, Size: 674", "Cluster4, Size: 1949", "Cluster5, Size: 1228"])




# naming the x axis 

plt.tight_layout()
plt.savefig("cluster_size.png", format="PNG")

graphic.graphic(net)



