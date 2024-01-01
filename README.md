# A Coding Challenge

I recently applied for a job that asked whether I'd be willing to complete a coding challenge.  The challenge in question was listed as **"hard"** on the programming site and after what seems like 4 years only 26% of the developers who attempted it have been able to solve it.  

I scored 100% - but I don't say that to brag.  After completing the test I was able to view the solutions my peers created... and mine is certainly not as elegant as some of the ones I saw!  That said, I'm still proud of my approach to a solution, and I thought it would be fun to share it here.

The core problem involves a turn-based simulation with six possible moves per turn and a potential of 30-50 turns. Thus, computing and storing all 1.41e+38 possible moves required to find the best move isn't feasible using a brute force search.

Therefore, the challenge requires the application of computer science concepts such as:

* [recursion](https://en.wikipedia.org/wiki/Recursion#:~:text=Recursion%20in%20computer%20programming%20is,simpler%20versions%20of%20the%20problem)
* [data structures](https://en.wikipedia.org/wiki/Data_structure) (particularily, [trees](https://en.wikipedia.org/wiki/Tree_(data_structure)))
* search algorithms such as [depth first search](https://en.wikipedia.org/wiki/Depth-first_search) and [backtracking](https://en.wikipedia.org/wiki/Backtracking).   
* [heuristics](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) such as [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

**Quick summary**
- You have a four lane bridge with one to four bikes at the start of the bridge.
- Your goal is to get a minimum number of bikes across the bridge.
- To complicate matters the bridge has pot holes that bikes have to navigate by moving left or right or jumping over them.
- Your challenge is to write a game AI that can get at least the minimum number of bikes accross the bridge.
- The programming site provides you a turn-based simulation that will allow you to test your AI.

See: [Deeper summary of the core challenges](documentation/deeper-summary.md)

## How I addressed this challenge
- [My general approach](documentation/approach.md)
- [My solution](documentation/solution.md)

## Further thoughts
Given more free time I'd like to implement a version that uses a distributed search across multiple CPU cores. Although, I do think that would be overkill for this problem. It's just a bit painful to realize that only one of my machine's 10 cores was working on the problem.

## Directory of project files
| File | Description |
| --- | --- |
| source/bike_ai.py | The AI that computes the best next move for each turn. |
| source/simulator.py | A module that manages the states of the simulator and also processes and scores potential moves.  Used by the `bike_ai.py` module and the `simulation_tester.py` module. |
| source/simulation_tester.py | A simulation tester that can be used to test the AI locally |
| source/simulations.py | A collection of test cases that can be used by the `simulation_tester.py` module.|
| source/state_search_space_tree.py | A modle that defines the state nodes and search space tree. |
| source/main.py | A script that is used to host the AI within a simulation. |
| source/graphviz.py | A module that can be used to generate a graphviz graph of the search tree. |

- Files in the `scripts` folder are used to manage a docker stack that hosts the AI and the simulation.  See the [Docker instructions](documentation/docker.md) for more information.
- Files in the `python-dev` folder are used to build the docker image that is used by the docker stack.