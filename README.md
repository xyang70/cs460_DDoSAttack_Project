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
* Scapy(Do NOT use pip to install this library, use [this method instead](https://scapy.readthedocs.io/en/latest/installation.html#current-development-version))

## TCP SYN Flood

## Slowloris
slowloris is a DoS attack invented by Robert "RSnake" Hansen[1](https://en.wikipedia.org/wiki/Slowloris_(computer_security)). This attack technique allows a single computer to take down a server with very little bandwidth but can perform destructive impacts. A brief workflow is described as follow:

1. Create around 1000 sockets connecting to the target.
2. For each socket, send a HTTP GET(without the ending character) to the target.
3. In a while loop, for each socket, send a http header"X-a ...". Check if there is any sockets timed out by the server, if so, recreate the sockets and establish the connectioin. At the end, sleep the process for 10 - 20 seconds.

#### Experiments and Result
* **Sender**<br>
A picture when the Slowloris program is running:
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/Screen%20Shot%202019-04-22%20at%207.02.13%20PM.png?raw=true)

Wireshark Capturing on sender's computer:
![](https://github.com/xyang70/cs460_DDoSAttack_Project/blob/master/readme_img/Screen%20Shot%202019-04-22%20at%207.46.19%20PM.png?raw=true)

## Perform Stress Testing

#### TCP SYN Flood

#### Slowloris

## Protecting Your Computer From these Attacks

#### TCP SYN Flood

#### Slowloris



## Conclusion




























## Reference

