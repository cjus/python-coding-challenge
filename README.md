# A Coding Challenge

I recently applied for a job that asked whether I'd be willing to complete a coding challenge.  The challenge in question was listed as **"hard"** on the programming site and after what seems like 4 years only 26% of the developers who attempted it have been able to solve it.  I scored 100% - but I don't say that to brag.  After completing the test I was able to view the solutions my peers created... and mine is certainly not as elegant as some of the ones I saw!  Also, the problem took me quite some time and effort to complete.  Part of the reason is that it's a computer science problem and I don't have a formal computer science education.  Although, I do have past game programming experience including in Chess AI - but that was also a long time ago!

The challenge requires the application of computer science concepts such as [recursion](https://en.wikipedia.org/wiki/Recursion#:~:text=Recursion%20in%20computer%20programming%20is,simpler%20versions%20of%20the%20problem), [data structures](https://en.wikipedia.org/wiki/Data_structure) (particularily, [trees](https://en.wikipedia.org/wiki/Tree_(data_structure))) and search algorithms such as [depth first search](https://en.wikipedia.org/wiki/Depth-first_search) and [backtracking](https://en.wikipedia.org/wiki/Backtracking).   Due to the complexity of the problem, it's not possible to [brute force](https://en.wikipedia.org/wiki/Brute-force_search) a solution.  The use of [heuristics](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) such as [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) are required to solve the problem in real-time.

> As a side note, even a family member's CS class at Dartmouth didn't seem to address all of those topics. Granted he may still encounter them later in his studies.

In my solution I also built a simulator that closely models the one online.  The simulator, included in this repo, uses [unix system pipes](https://en.wikipedia.org/wiki/Pipeline_(Unix)) to communicate with the client application which hosts the game AI.  This wasn't required but I had time on my hands and having control of both ends of the problem made it easier to debug and test my solution.

**Quick summary**
- You have a four lane bridge with one to four bikes at the start of the bridge.
- Your goal is to get a minimum number of bikes accross the bridge.
- To complicate matters the bridge has pot holes that bikes have to navigate by moving left or right or jumping over them.
- Your challenge is to write an AI that can get at least the minimum number of bikes accross the bridge.
- The programming site provides you a turn-based simulation that will allow you to test your AI.

## Core challenges

- During each turn (iteration on the game loop) you're given the updated position of your bikes and the speed they're traveling.
- On each turn you must provide your next move.
- You can't take moves back once you've made them and when you lose a bike it's gone for good.
- With six possible moves per turn and a potential of 30-50 turns, computing and storing all 1.41e+38 possible moves required to find the best move is not feasible using a brute force search.
  - According to ChatGPT: 
    - That's one quintillion, four hundred ten sextillion or 1,410,000,000,000,000,000,000,000,000,000,000,000,000,000. 
    - *It's approximately the estimated number of atoms in the observable universe, which is about 10^80. This comparison highlights the immense magnitude of such a number.*
      - Note this is probably only true from Earth and doesn't take into account the universe revealed by the Webb space telescope. But alas we digress :-D

So the fundemental challenge is that on each turn you have to compute the best next move given the information at hand while drastically minimizing the size of the search tree and thus time to a solution.

## Deeper dive
- [My general approach](documentation/approach.md)
- [My solution](documentation/solution.md)

## Further thoughts
Given more free time I'd like to implement a version that uses a distributed search accross multiple CPU cores. Although, I do think that would be overkill for this problem. It's just a bit painful to realize that only one of my machine's 10 cores was working on the problem.

## Directory of project files
| File | Description |
| --- | --- |
| [bike_ai.py](source/bike_ai.py) | The AI that computes the best next move for each turn. |
| [simulator.py](source/simulator.py) | A module that manages the states of the simulator and also processes and scores potential moves.  Used by the `bike_ai.py` module and the `simulation_tester.py` module. |
| [simulation_tester.py](source/simulation_tester.py) | A simulation tester that can be used to test the AI locally |
| [simulations.py](source/simulations.py) | A collection of test cases that can be used by the `simulation_tester.py` module.|
| [state_search_space_tree.py](source/state_search_space_tree.py) | A modle that defines the state nodes and search space tree. |
| [main.py](source/main.py) | A script that is used to host the AI within a simulation. |
| [graphviz.py](source/graphviz.py) | A module that can be used to generate a graphviz graph of the search tree. |

- Files in the `scripts` folder are used to manage a docker stack that hosts the AI and the simulation.  See the [Docker instructions](documentation/docker.md) for more information.
- Files in the `python-dev` folder are used to build the docker image that is used by the docker stack.