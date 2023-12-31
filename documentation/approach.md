# My general approach
I approached this problem by first ensuring I understood how the online simulator works, i.e., how it interpretes the use of the six possible moves per turn.

To do this I first built a `simulation_tester.py` module which is functionally similar to the online one - even in how it uses operating system pipes to communicate with the child process that hosts the client AI.

The online site provides a series of test cases that you can use to test your AI.  I encoded those test cases in my `simulations.py` module which is used by my `simulation_tester.py` module. This allowed me to iterate on my AI locally without having to use the online site. I considered that necessary in order to be able to debug my AI, but also to be able to test my AI with shorter and custom test cases.

Personally, I like to use docker containerized environments and Visual Studio Code's remote development features to build my projects.  This allows me to use my local IDE and tools while still having a consistent environment for my projects.

## Simulation console output

By building a local simulation tester I was able to capture the console output of the simulation.  This allowed me to see the state of the game at each turn and to see the moves that were being made by my AI.  This was very helpful in debugging my AI.

![Console output of simulation tester](./console-out-01.png)

In the above example we see that an earlier version of the AI found two winning moves but took 70 seconds to do so on a Mac M1 MAX Pro. Part of the problem was that it had to create and evaluate 2.9 millions nodes out of a possible 12 million nodes at the 9th ply.

In this example, the AI found the winning move in 0.0108 seconds by only evaluating 208 nodes out of a possible 731,231,688,012,594 nodes at the 19th ply.

```shell
Starting Bike_AI on Sim 12: Well worn road

Found a winning line at node (161) with a score of 0.81 in 0.0108 seconds
        ['SPEED', 'DOWN', 'SPEED', 'UP', 'JUMP', 'UP', 'SLOW', 'DOWN', 'DOWN', 'SPEED', 'JUMP', 'UP', 'SPEED', 'SPEED', 'JUMP', 'UP', 'UP', 'SPEED', 'JUMP', 0.81]
... adding node 208
Bike_AI elapsed time: 0.01 seconds.
Examined a total of 208 nodes out of a maximum possible 731,231,688,012,594 nodes by depth: 19
Winning line is: ['SPEED', 'DOWN', 'SPEED', 'UP', 'JUMP', 'UP', 'SLOW', 'DOWN', 'DOWN', 'SPEED', 'JUMP', 'UP', 'SPEED', 'SPEED', 'JUMP', 'UP', 'UP', 'SPEED', 'JUMP', 0.81]
```

Here is the console output per iteration:

At the starting position there are two bikes.

```shell
Speed: 1
00000000001111111111222222222233333333334444444444555555555566666
01234567890123456789012345678901234567890123456789012345678901234
-----------------------------------------------------------------
................xxxxxxxxx........xxxxx........xxx.............xx.
1x.x..................xxx....xxx......x.x..................xxxxx.
2...xxx.........x.x...xxx................xxx............xxxxxx.x.
............x.xxxxxx...........xxxx...............x.x.....xxxxxx.
```


- [Docker instructions](documentation/docker.md)
