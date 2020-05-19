import numpy as np

def expected_duration(n):
     n_coins = n
     n_rounds = 0
     while n_coins > 0:
          flips = np.random.randint(2, size=n_coins)
          n_tails = flips.sum()
          n_coins -= n_tails
          n_rounds+=1
    
     return n_rounds

print(expected_duration(10))

