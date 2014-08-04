route-smash
===========

Quick'n'Dirty prefix generator for use with ExaBGP

### Description

This is a simple python script to generate sequential BGP updates (all /24s).  When combined with an appropriate ExaBGP configuration, route-smash can be used to load test routers and benchmark RIB, FIB and Forwarding-Plane limits.

### Usage

Given the following exabgp configuration:


```
## File: exabgp.conf
neighbor 10.0.5.10 {
    description "Test Router";
    router-id 10.0.0.31;
    local-address 10.0.0.31;
    local-as 65001;
    peer-as 65000;
    process route-smash {
    	run ./route-smash.py;
    }
}
```

and assuming route-smash.py was located in the same directory you would launch with:

```
exabgp exabgp.conf
```
