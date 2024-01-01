# A deeper summary of the core challenges

> ⤴️ [README.md](../README.md#how-i-addressed-this-challenge)


- During each turn (iteration on the game loop) you're given the updated position of your bikes and the speed they're traveling.
- On each turn you must provide your next move.
- You can't take moves back once you've made them and when you lose a bike it's gone for good.
- With six possible moves per turn and a potential of 30-50 turns, computing and storing all 1.41e+38 possible moves required to find the best move is not feasible using a brute force search.
  - According to ChatGPT: 
    - That's one quintillion, four hundred ten sextillion or 1,410,000,000,000,000,000,000,000,000,000,000,000,000,000. 
    - *It's approximately the estimated number of atoms in the observable universe, which is about 10^80. This comparison highlights the immense magnitude of such a number.*
      - Note this is probably only true from Earth and doesn't take into account the universe revealed by the Webb space telescope. But alas we digress :-D

So the fundemental challenge is that on each turn you have to compute the best next move given the information at hand while drastically minimizing the size of the search tree and thus time to a solution.
