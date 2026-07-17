'''
Count how many times a coin lands on heads/tails (use random).
'''
import random
turn_count = int(input("Enter the number of times to flip the coin: "))
heads_count = 0
tails_count = 0
for _ in range(turn_count):
    flip = random.randint(0, 1)
    if flip == 0:
        heads_count += 1
    else:
        tails_count += 1
print(f"Number of heads: {heads_count}")
print(f"Number of tails: {tails_count}")
