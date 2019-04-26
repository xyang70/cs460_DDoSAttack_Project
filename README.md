# UIUC CS460 DDoS Attack Final Project
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
* [TP-Link TL-WDR7300](https://www.tp-link.com.cn/product_1039.html)<br>

One of the Raspberry Pi is used as a victim with apache as the experimental server; the other computers are either used as senders or acted as a normal user.
#### Software
* Python 3.7/ Python 2.7 (scapy library has issues while running on different platforms)
* Scapy(Do NOT use pip to install this library, use this [method](https://scapy.readthedocs.io/en/latest/installation.html#current-development-version) instead) 
#### Program Flowchart<br>
Left side is the workflow for the main sender, right side is the workflow for the bots.
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/Program%20flowchart.png?raw=true)
#### Performing Stress Testing
To perform stress testing program, run the following command:<br>
* Intel/AMD Platform:
```
$sudo python3 main.py
```
* Arm Platform:
```
$sudo python2 main.py
```
Follow the prompt and enter the target IP address, port, and the option to enable muli-threading. The program should run momentarily.
## TCP SYN Flood
[TCP SYN Flood](https://www.imperva.com/learn/application-security/syn-flood/?utm_campaign=Incapsula-moved) is a DoS attack by exploiting the three-way handshakes between the client and the server. In details, TCP SYN Flood works as the following:
1. Sender sends a "SYN" request to the target.
2. Target responds with a "SYN-ACK" packet back to the sender, and waiting for an "ACK" packet from the sender.
3. Sender disregard the "SYN-ACK" packet and do something else.
4. Target is still waiting for the "ACK" packet until ttl(time to live) is reached.
5. Many bot computers repeat the same step 1 to 4 every millisecond, making the target out of resources to handle the real requests from other human users. Hence, making human users unable to connect to the target.

#### Experiments and Result
>Note:<br>
>There was issue running the ssh feature(library pexpect will raise timeout exception when the bots are running script without >response), I have disabled such features. Instead, I put all senders under the same network and manually ran the program.<br>
>
Due to TP-Link 5 Port Network Switch(TL-SG105) is a unmanged switch, hence, there are packets getting misrouted to other senders, leading to a decrease in performance, I decided to change it to TP-Link TL-WDR7300,a wireless router, with 3 senders using ethenet, and the target using wireless network. A physical connection is as follow:
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/IMG_2802.jpg?raw=true)
Before the stress test begins, all users could visit the website as follow:
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/Screen%20Shot%202019-04-26%20at%2012.11.09%20AM.png?raw=true)
* **Sender**<br>
  Sender will not output anything to the console inorder to acheive the best performance.
* **Target(192.168.0.101)**<br>
  I used tcptrack to track the internet connections, a command is follow:
  ```
  $sudo tcptrack -i wlan0  #wlan0 means the wireless interface of Raspberry Pi
  ```
  After all 3 senders had been running for about 30 minutes, the target has received 23,189 connections with false source IP and port(IP address spoofing, yes, I have randomly generated IPs and ports). The serivce was down, and no other visitors could visit the website 192.168.0.101 .<br>
  ![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/IMG_5052.jpg?raw=true)
  After I had shut down all senders, the target was stabled with 21,665 connections. But no other visitors(except the senders) could visit the website.
* **Normal Visitors**
  At 30 minutes mark, other devices can not normally visit the apache default welcome page. Instead, they see these:
  * From Ipad 2018
  ![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/IMG_0022.PNG?raw=true)
  * From Windows 10
  ![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/TCP.PNG?raw=true)
  
## Slowloris
[Slowloris](https://en.wikipedia.org/wiki/Slowloris_(computer_security)) is a DoS attack invented by Robert "RSnake" Hansen. This attack technique allows a single computer to take down a server with very little bandwidth but can perform destructive impacts. A brief workflow is described as follow:

1. Create around 1000 sockets connecting to the target.
2. For each socket, send a HTTP GET(without the ending character) to the target.
3. In a while loop, for each socket, send a http header"X-a ...". Check if there is any sockets timed out by the server, if so, recreate the sockets and establish the connectioin. At the end, sleep the process for 10 - 20 seconds.


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
* **[Increase Server Avalability](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/)**<br>
  Increase the number of connections that are allowed from the server. But one computer can use 65,535 ports to connect to a server, hence, this fix is not really pratical.
* **Limit the Number of Connections by IP Address**<br>
  Limit the number of connections for an IP Address can prevent DoS, but not in Distributed DoS.
* **Restrict Connection Time**<br>
  Restrict the connection time can kill many unnecessary connections.
* **Install Protecting Software**<br>
  There are useful tools such as libapache2-mod-qos and mod-security can help preventing Slowloris.

## Conclusion
DDoS attack is still an [unsolvable problem](https://www.zhihu.com/question/26741164) in network security after many years. What the protectors can do are to prevent the attacks and reduce the damage. Many sites have hired professional network security service to prevent DDoS. But in social engineering, how to not to be an attacker is the root of the cause.

