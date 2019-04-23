# UIUC CS460 DDoS Attack Project

## Environment Setup

## TCP SYN Flood

## Slowloris
slowloris is a DoS attack invented by Robert "RSnake" Hansen[1](https://en.wikipedia.org/wiki/Slowloris_(computer_security)). This attack technique allows a single computer to take down a server with very little bandwidth but can perform destructive impacts. A brief workflow is described as follow:

1. Create around 1000 sockets connecting to the target.
2. For each socket, send a HTTP GET(without the ending character) to the target.
3. In a while loop, for each socket, send a http header"X-a ...". Check if there is any sockets timed out by the server, if so, recreate the sockets and establish the connectioin. At the end, sleep the process for 10 - 20 seconds.

#### Experimental Result

## Protecting Your Computer From theses Attacks

#### TCP SYN Flood

#### Slowloris



## Conclusion




























## Reference

