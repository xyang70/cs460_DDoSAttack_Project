# UIUC CS460 DDoS Attack Project
>Note:<br>
>This experiment was performed on a local network,
>there was no harm to other users on the Internet while this experient was conducting.
## Environment Setup

#### Hardware
* Macbook Pro Early 2015 Running on Mac OS Mojave 10.14.4
* 2 x Raspberry Pi Model 3 B+ Running on Debian Stretch with Raspberry Pi Desktop
* Laptop Running on Ubuntu 16.04
* TP-Link 5 Port Gigabit Ethernet Network Switch(TL-SG105)
* Ethernet Cat-6 cables<br>

One of the Raspberry Pi is used as a victim with apache as the experimental server; the other computers are either used as senders or acted as a normal user.
#### Software
* Python 3.7/ Python 2.7 (scapy library has issues while running on different platforms)
* Scapy(Do NOT use pip to install this library, use this [method](https://scapy.readthedocs.io/en/latest/installation.html#current-development-version) instead) 
#### Program Flowchart<br>
Left side is the workflow for the main sender, right side is the workflow for the bots.
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/Program%20flowchart.png?raw=true)
## TCP SYN Flood
[TCP SYN Flood](https://www.imperva.com/learn/application-security/syn-flood/?utm_campaign=Incapsula-moved) is a DoS attack by exploiting the three-way handshakes between the client and the server. In details, TCP SYN Flood works as the following:
1. Sender sends a "SYN" request to the target.
2. Target responds with a "SYN-ACK" packet back to the sender, and waiting for an "ACK" packet from the sender.
3. Sender disregard the "SYN-ACK" packet and do something else.
4. Target is still waiting for the "ACK" packet until ttl(time to live) is reached.
5. Many bot computers repeat the same step 1 to 4 every millisecond, making the target out of resources to handle the real requests from other human users. Hence, making human users unable to connect to the target.

#### Experiments and Result

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

  Wireshark Capture on sender's computer:
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
* [**Use SYN Cookies**](https://en.wikipedia.org/wiki/SYN_cookies)<br>
  Using SYN Cookies can avoid SYN flood because the server will send "SYN-ACK" back to the client and discard the "SYN" entry from the SYN queue. If the client respond back with an "ACK", then the server will reconstruct SYN queue and establish connection.
* **Decrease ttl on the Server**<br>
  Since the main vulnerability of the server is out of resources, hence, a server can be configured to have less time to live(ttl) for each connection, making sure the connection is disconnected at a given time to release resources.
* **
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
