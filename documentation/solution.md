# My Solution

This type of challenges use a search algorithm to compute the best next move for each turn based on the current state of the game. This is commonly done using a search state tree of possible moves and then uses a heuristic to determine the best move.  

In my solution when a winning move is found it's returned immediately. Even if it's not the best move. This is necessary because the simulation will terminate the game if the AI doesn't return a move within a certain amount of time. That said, my solution has a `full_search`` flag on the `Bike_AI` class that will force the AI to search the entire tree before returning a move. This is useful for debugging and testing but can't be used in production.

```python
Bike_AI(simulator, use_graphviz=False, debug=False, full_search=False)
```

## Core AI files

| File | Description |
| --- | --- |
| [bike_ai.py](bike_ai.py) | The AI that computes the best next move for each turn. |
| [simulator.py](simulator.py) | A module that manages the states of the simulator and also processes and scores potential moves.  Used by the `bike_ai.py` module and the `simulation_tester.py` module. |
| [state_search_space_tree.py](state_search_space_tree.py) | A modle that defines the state nodes and search space tree. |

