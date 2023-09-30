Process Scheduling
==================

* I/O-bound vs Processor-Bound process
	* I/O -bound: Keyboard input, network I/O, disk I/O, graphical user interface (GUI)
	* Processor-bound: spend most of their time executing code. They tend to run until they are preempted becuase they do not block on I/O requests very often.
		* ssh-keygen
		* MATLAB

* Purpose of scheduling policy: attempt to satisfy two conflicting goals
	* Fast process response time: Low Latency
	* Maximal system utilization: High Throughput
* Process priority:
	* Nice value: -20 --> +19
	* Real-timep priority: 0 --> 99

* Timeslice:
	* Too long timeslice: 
		* system have poor interactive performance
		* system will no longer feel as if applications are concurrently executed
	* Too short timeslice:
		* significant amount of processor time to be wasted on the overhead of switching processs

* CFS: Complete Fair Scheduling
	* Attempt to give all processes a fair share of the processor

* Schedule class:
	* Base schedule code iterate over each scheduler class in order of priority: kernel/sched.c
	* CFS is the registered scheduler class for normal process: kernel/sche_fair.c

Link:

* https://github.com/ianohara/linux-rt-examples
* https://man7.org/tlpi/code/online/dist/procpri/demo_sched_fifo.c.html
* https://wiki.linuxfoundation.org/realtime/documentation/howto/applications/application_base
