# Ansible Initial Setup on GNS3

<img src="https://i.imgur.com/20wwfZB.png" alt="Topology">

## Configuration for OpenvSwitchManagement:
```shell
#DHCP config for eth1
auto eth1
iface eth1 inet dhcp
```
Don't use port eth0 as it purpose is for port management.

## Configuration for Router R1

```Cisco
int eth0/0
no shut
ip add 192.168.122.100 255.255.255.0
end
```
**Config username and SSH**
```Cisco
username user password user123
username user privilege 15
ip domain-name packetnotes.com
line vty 0 4
transport input all
login local
!
crypto key generate rsa
The name for the keys will be: R1.packetnotes.com
Choose the size of the key modulus in the range of 360 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [512]: 1024
% Generating 1024 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 1 seconds)
!
exit
```

## Configuration for Network Automation Device
```shell
root@NetworkAutomation:~# cat /etc/network/interfaces

#
# This is a sample network config uncomment lines to configure the network
#

# Static config for eth0
#auto eth0
#iface eth0 inet static
#       address 192.168.0.2
#       netmask 255.255.255.0
#       gateway 192.168.0.1
#       up echo nameserver 192.168.0.1 > /etc/resolv.conf

# DHCP config for eth0
 auto eth0
 iface eth0 inet dhcp
root@NetworkAutomation:~#
```
Then stop and start device to get the DHCP address.

## Configure Hosts File

**Directory /etc**
```shell
root@NetworkAutomation:/etc# ls -al | grep hosts
-rwxr-xr-x 1 root root     178 May  9 10:16 hosts

root@NetworkAutomation:/etc# cat hosts
127.0.1.1       NetworkAutomation
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

```
## Edit file hosts in /etc/ to add R1 ip address

```shell
root@NetworkAutomation:/etc# nano hosts

```
<img src="https://i.imgur.com/Bf6LanV.png" alt="Add R1 ip address">

**Ping to R1**

- With DNS
```shell
root@NetworkAutomation:~# ping R1
PING R1 (192.168.122.100) 56(84) bytes of data.
64 bytes from R1 (192.168.122.100): icmp_seq=1 ttl=255 time=3.51 ms
64 bytes from R1 (192.168.122.100): icmp_seq=2 ttl=255 time=1.97 ms
^C
--- R1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1005ms
rtt min/avg/max/mdev = 1.978/2.748/3.518/0.770 ms
```

- Or ping with IP address
```shell
root@NetworkAutomation:/etc# ping 192.168.122.100
PING 192.168.122.100 (192.168.122.100) 56(84) bytes of data.
64 bytes from 192.168.122.100: icmp_seq=1 ttl=255 time=3.68 ms
64 bytes from 192.168.122.100: icmp_seq=2 ttl=255 time=1.30 ms
^C
--- 192.168.122.100 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 1.309/2.499/3.689/1.190 ms
root@NetworkAutomation:/etc#
```

**Check if there is any already configured host.**
```shell
root@NetworkAutomation:~# ansible --list-hosts all
 [WARNING]: provided hosts list is empty, only localhost is available. Note
that the implicit localhost does not match 'all'

  hosts (0):
root@NetworkAutomation:~#
```

## Edit file /etc/hosts and add more hosts
```shell
- 192.168.122.100 R1
- 192.168.122.101 R2
- 192.168.122.103 S1
- 192.168.122.104 S2

- 192.168.122.183 Server1
```

<img src="https://i.imgur.com/TNIELaF.png" alt="Add more hosts">

**Try to ping R2**
```shell
Coba Ping R2

root@NetworkAutomation:~# ping R2
PING R2 (192.168.122.101) 56(84) bytes of data.
From 192.168.122.10 icmp_seq=1 Destination Host Unreachable
From 192.168.122.10 icmp_seq=2 Destination Host Unreachable
From 192.168.122.10 icmp_seq=3 Destination Host Unreachable
^C
--- R2 ping statistics ---
5 packets transmitted, 0 received, +3 errors, 100% packet loss, time 3999ms
pipe 4
root@NetworkAutomation:~#
```

## Create host file on root directory

```shell
root@NetworkAutomation:~# nano hosts
```
<img src="" alt="">

```shell
root@NetworkAutomation:~# ls
hosts
root@NetworkAutomation:~# cat hosts
[gns3-ios]
R1
R2
S1
S2
root@NetworkAutomation:~#
```

## Create ansible configuration file at root directory
<img src="" alt="">

```shell
[defaults]
hostfile = ./hosts
host_key_checking = false
timeout = 5
```
