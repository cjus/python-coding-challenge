# A Coding Challenge

I recently applied for a job that asked whether I'd be willing to complete a coding challenge. åThe challenge was hosted on a a programming site with the following description (note I've changed the wording to protect the challenge for future developers):

It's the sort of problem that reminds you of all those things you learned in school but never thought you'd use in the real world. It's also the sort of problem that you can't brute force your way through. You have to think about the problem and come up with a solution that is both efficient and effective.

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
- With six possible moves per turn and a potential of 30-50 turns, computing and storing all 1.41e+38 possible moves required to find the best move is not feasible using a [brute force search](https://en.wikipedia.org/wiki/Brute-force_search).
  - According to ChatGPT: 
    - That's one quintillion, four hundred ten sextillion or 1,410,000,000,000,000,000,000,000,000,000,000,000,000,000. 
    - *It's approximately the estimated number of atoms in the observable universe, which is about 10^80. This comparison highlights the immense magnitude of such a number.*
      - Note this is probably only true from Earth and doesn't take into account the universe revealed by the Webb space telescope. But alas we digress :-D

So the fundemental challenge is that on each turn you have to compute the best next move given the information at hand while drastically minimizing the size of the search tree and thus time to a solution.

## Deeper dive
- [My general approach](documentation/approach.md)
- [My solution](documentation/solution.md)

## Directory of project files
| File | Description |
| --- | --- |
| [bike_ai.py](bike_ai.py) | The AI that computes the best next move for each turn. |
| [simulator.py](simulator.py) | A module that manages the states of the simulator and also processes and scores potential moves.  Used by the `bike_ai.py` module and the `simulation_tester.py` module. |
| [simulation_tester.py](simulation_tester.py) | A simulation tester that can be used to test the AI locally |
| [simulations.py](simulations.py) | A collection of test cases that can be used by the `simulation_tester.py` module.|
| [state_search_space_tree.py](state_search_space_tree.py) | A modle that defines the state nodes and search space tree. |
| [main.py](main.py) | A script that is used to host the AI within a simulation. |
| [graphviz.py](graphviz.py) | A module that can be used to generate a graphviz graph of the search tree. |

- Files in the `scripts` folder are used to manage a docker stack that hosts the AI and the simulation.  See the [Docker instructions](documentation/docker.md) for more information.
- Files in the `python-dev` folder are used to build the docker image that is used by the docker stack.