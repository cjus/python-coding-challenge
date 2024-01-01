# My Solution

> ⤴️ [README.md](../README.md#how-i-addressed-this-challenge)

These types of challenges require the use of a search algorithm to compute the best next move for each turn based on the current state of the game. This is commonly done using a search tree consisting of possible moves and the uses a heuristic to determine the best move.  

The challenge requires the application of computer science concepts such as [recursion](https://en.wikipedia.org/wiki/Recursion#:~:text=Recursion%20in%20computer%20programming%20is,simpler%20versions%20of%20the%20problem), [data structures](https://en.wikipedia.org/wiki/Data_structure) (particularily, [trees](https://en.wikipedia.org/wiki/Tree_(data_structure))) and search algorithms such as [depth first search](https://en.wikipedia.org/wiki/Depth-first_search) and [backtracking](https://en.wikipedia.org/wiki/Backtracking).   Due to the complexity of the problem, it's not possible to [brute force](https://en.wikipedia.org/wiki/Brute-force_search) a solution.  The use of [heuristics](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) such as [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) are required to solve the problem in real-time.

> As a side note, even a family member's CS class at Dartmouth didn't seem to address all of those topics. Granted he may still encounter them later in his studies.

I also built a simulator that closely models the one online.  The simulator, included in this repo, uses [unix system pipes](https://en.wikipedia.org/wiki/Pipeline_(Unix)) to communicate with the client application which hosts the game AI.  This wasn't required but I had time on my hands and having control of both ends of the problem made it easier to debug and test my solution.

## State representation
As I initially thought through the problem I realized I'd have to do a fair amount of complex testing. So I realized early on that I wanted to represent game states using immutable objects.
That would allow me to safely playback move states for debugging!

I created a `SimulatorState` (simulator.py) which has a `Simulator.clone()` member function that returns a new instance of the state.  This is used by the simulator to create a new state for each move.  

A `SimulatorState` is used by the `Simulator.render()` method to render the state of the game to the console.  That makes it possible to graphically render a game state to the console which is great for debugging and testing.

```shell
Processing: SPEED
Speed: 6
00000000001111111111222222222233333333334444444444555555555566666
01234567890123456789012345678901234567890123456789012345678901234
-----------------------------------------------------------------
................xxxxxxxxx........xxxxx........xxx............2xx.
.1.x..................xxx....xxx......x.x..................xxxxx.
....xxx.........x.x...xxx................xxx............xxxxxx.x.
............x.xxxxxx...........xxxx...............x.x.....xxxxxx.
```

The `Simulator.process()` method is used to process a move and return a new state.  The Simulator.process() method is also used by the AI to process potential moves and score them.
›

## Tree representation
Having chosen to use immutable states I realized my tree implementation would be a [State Space Search Tree](https://en.wikipedia.org/wiki/State_space_search).

![State Space Search Tree](./search-tree.png)
> The above diagram was created with [GraphViz](#graphviz), which I discuss below.  A PDF of a larger graph can be found [here](./search-tree.pdf). Note you'll need a PDF viewer that allows you to zoom in to see the details.

## Move search cut-off

In my solution when a winning move is found it's returned immediately. Even if it's not the best move. This is necessary because the simulation will terminate the game if the AI doesn't return a move within a certain amount of time. That said, my solution has a `full_search` flag on the `Bike_AI` class that will force the AI to search the entire tree before returning a move. That was useful for debugging and testing but can't be used in production.

```python
Bike_AI(simulator, use_graphviz=False, debug=False, full_search=False)
```

## Depth first search

I used a [depth first search algorithm](https://en.wikipedia.org/wiki/Depth-first_search) to build the search tree.  This is a common approach for these types of problems.  It's particularily important in my solution because this allows for a move sequence to be evaluated and for the evaluation score to be used to eliminate other potential moves.
See my note on `alpha-beta pruning` below.

## The heuristic

In order to constrain the size of the search tree I used a heuristic that scores each potential move.  Below is the score code snipit:

```python
  child_state = self.simulator.process(new_state)
  score = child_state.remaining_bikes - ((node.depth + 1) * 0.01)
  if score < self.highest_score:
      continue
```

The heuristic scores a potential move based on the number of bikes remaining after a move. A penalty is then applied based on the depth of the move in the search tree. That results in scores that favors more bikes crossing the bridge earlier, i.e., sorter solutions.

The best score identified is then used to eliminate all other potential moves that have a lower score.  This is a common technique, called [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning), that is used to reduce the size of the search trees.

## Useful tools
#### Graphviz
Early on I wanted to visualize the search tree to help me debug and understand the AI's behavior.  I used the [graphviz](https://graphviz.org/) library to generate a graph of the search tree. I built the `graphviz.py` wrapper module for this purpose.  The `Bike_AI` class has a `use_graphviz` flag that can be used to enable/disable the graphviz graph generation. Note that after about 5-10 turns the graph becomes too large to be useful.  This is where I generated custom test cases to help limit the size of the graph.

#### Apple Freeform
I also used [Apple's Freeform](https://apps.apple.com/us/app/freeform/id6443742539) to visually think through challenges using a digital whiteboard.

![Apple Freeform visualization of moves](./apple-freeform.png)

## Core AI files
The following files make up the core AI.

| File | Description |
| --- | --- |
| source/bike_ai.py | The AI that computes the best next move for each turn. |
| source/simulator.py | A module that manages the states of the simulator and also processes and scores potential moves.  Used by the `bike_ai.py` module and the `simulation_tester.py` module. |
| source/state_search_space_tree.py | A module that defines the state nodes and search space tree. |

> ⤴️ [README.md](../README.md#how-i-addressed-this-challenge)
