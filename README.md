# disktest

Disclaimer: Doing tests with raw disks is always dangerous,
use this application against raw disks if you really know what
you are doing. Author is not responsible about the possible
data losses caused by this software.


This application is written to help us test the disk systems.

Main purpose is to find out the bottlenecks in the whole system,
where the performance is capped because of the internal structure
of the devices tested.

We are using linux dd command to do the tests. It is very easy
to add raw disks and destroy data inside irreversably if you provide
the wrong device names. Please do not use this application on
systems with important data.
