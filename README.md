# A Coding Challenge

I recently applied for a job that asked whether I'd be willing to complete a coding challenge.  The challenge was hosted on a a programming site with the following description (note I've changed the wording to protect the challenge for future developers):

- You have a four lane bridge with one to four bikes at the start of the bridge.
- Your goal is to get a minimum number of bikes accross the bridge.
- To complicate matters the bridge has pot holes that bikes have to navigate by moving left or right or jumping over them.
- Your challenge is to write an AI that can get at least the minimum number of bikes accross the bridge.
- The programming site provides you a turn-based simulation that will allow you to test your AI.

## Core challenges

- During each turn (iteration on the game loop) you're given the updated position of your bikes and the speed they're traveling.
- On each turn you must provide your next move.
- You can't take moves back once you've made them and when you lose a bike it's gone for good.
- With six possible moves per turn and a potential of 30-50 turns, computing and storing all 1.41e+38 possible moves required to find the best move is not feasible using brute force search on most single machines.

So the core challenge is that on each turn you have to compute the best next move given the information at hand while minimizing the size of the search tree.

## My general approach
I approached this problem by first ensuring I understood how the online simulator works, i.e., how it interpretes the use of the six possible moves per turn.

To do this I built a `simulation_tester.py` module which is functionally similar to the online one - even in how it uses operating system pipes to communicate with the child process that hosts the client AI.

The online site provides a series of test cases that you can use to test your AI.  I encoded those test cases in my `simulations.py` module which is used by my `simulation_tester.py` module. This allowed me to iterate on my AI locally without having to use the online site.

I considered that necessary in order to be able to debug my AI, but also to be able to test my AI with shorter and custom test cases.


## My solution
- [My solution](documentation/solution.md)




## Docker Setup
- [Docker instructions](documentation/docker.md)

