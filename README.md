# UIUC CS460 DDoS Attack Project

## Environment Setup

#### Hardware
* Macbook Pro Early 2015 Running on Mac OS Mojave 10.14.4
* 2 x Raspberry Pi Model 3 B+
* Laptop Running on Ubuntu 16.04
* TP-Link 5 Port Gigabit Ethernet Network Switch(TL-SG105)
* Ethernet Cat-6 cables

#### Software
* Python 3.7/ Python 2.7 (scapy library has issues while running on different platforms)
* Scapy(Do NOT use pip to install this library, use this [method](https://scapy.readthedocs.io/en/latest/installation.html#current-development-version) instead) 
#### Program Flowchart
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/Program%20flowchart.png?raw=true)
## TCP SYN Flood

## Slowloris
[Slowloris](https://en.wikipedia.org/wiki/Slowloris_(computer_security)) is a DoS attack invented by Robert "RSnake" Hansen. This attack technique allows a single computer to take down a server with very little bandwidth but can perform destructive impacts. A brief workflow is described as follow:

1. Create around 1000 sockets connecting to the target.
2. For each socket, send a HTTP GET(without the ending character) to the target.
3. In a while loop, for each socket, send a http header"X-a ...". Check if there is any sockets timed out by the server, if so, recreate the sockets and establish the connectioin. At the end, sleep the process for 10 - 20 seconds.

#### Performing Stress Testing

#### Experiments and Result
* **Sender**<br>
A picture when the Slowloris program is running:
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/Screen%20Shot%202019-04-22%20at%207.02.13%20PM.png?raw=true)

Wireshark Capturing on sender's computer:
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/Screen%20Shot%202019-04-22%20at%207.46.19%20PM.png?raw=true)
* **Target**<br>
The target does have significant CPU usage changes, insteads, it receives many connection request from the sender.<br>
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/IMG_4820.jpg?raw=true)
* **Normal Visitors**<br>
  Before slowloris, everything works fine:
  ![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/IMG_6144.jpg?raw=true)
  In slowloris, connection is slowing down:
  ![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/IMG_8434.jpg?raw=true)
  After slowloris used all resources:
  ![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/IMG_0950.jpg?raw=true)


## Protecting Your Computer From these Attacks

#### TCP SYN Flood

#### Slowloris
* **Platform Dependency**<br>
  Slowloris is designed for apache server, using different servers will greatly reduce the chance of being Slowloris DoS.
* **Increase Server Avalability[2]**<br>
  Increase the number of connections that are allowed from the server. But one computer can use 65,535 ports to connect to a server, hence, this fix is not really pratical.
* **Limit the Number of Connections by IP Address**<br>
  Limit the number of connections for an IP Address can prevent DoS, but not in Distributed DoS.
* **Restrict Connection Time**<br>
  Restrict the connection time can kill many unnecessary connections.
* **Install Protecting Software**<br>
  There are useful tools such as libapache2-mod-qos and mod-security can help preventing Slowloris.

## Conclusion
Hire cloud base protection



























## Reference
https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/
