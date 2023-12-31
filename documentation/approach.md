# My general approach
I approached this problem by first ensuring I understood how the online simulator works, i.e., how it interpretes the use of the six possible moves per turn.

To do this I built a `simulation_tester.py` module which is functionally similar to the online one - even in how it uses operating system pipes to communicate with the child process that hosts the client AI.

The online site provides a series of test cases that you can use to test your AI.  I encoded those test cases in my `simulations.py` module which is used by my `simulation_tester.py` module. This allowed me to iterate on my AI locally without having to use the online site. I considered that necessary in order to be able to debug my AI, but also to be able to test my AI with shorter and custom test cases.

As a personal preference, I like to use docker containerized environments and Visual Studio Code's remote development features to build my projects.  This allows me to use my local IDE and tools while still having a consistent environment for my projects.

- [Docker instructions](documentation/docker.md)
