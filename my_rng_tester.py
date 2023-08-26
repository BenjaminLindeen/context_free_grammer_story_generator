from my_rng import *
set_seed(101)
for i in range(10):
    print(next())

# 1697507
# 612712738
# 678900201
# 695061696
# 1738368639
# 246698238
# 1613847356
# 1214050682
# 1307682227
# 867545791

# due to lack of a specific equation -- can't FIRMLY test the next_int function.
# here are some _basic_ checks.

counts={}
for i in range(10000):
    # Just picking two numbers more-or-less at random.
    n = next_int(33, 45)
    counts[n] = counts.get(n,0)+1
print(min(counts)) # 33
print(max(counts)) # 45

for i in range(33,46):
    # So this isn't guaranteed but it should be true the vast majority of the time.
    # Based on some simulations -- ~99% of the time all counts should be between 700 and 840.
    # Ideally they should mostly be around 730-810
    print(i, counts[i], 680 < counts[i] < 860)

# Again -- due to lack of a specific equation like we had for next I can't give you FIRM tests.
options = ["apple", "bog", "fox", "dog", "bee"]

counts={}
for i in range(10000):
    op = random_choice(options)
    counts[op] = counts.get(op,0)+1
for op in options:
    # So this isn't guaranteed but it should be true the vast majority of the time.
    # Based on some simulations -- ~99% of the time all counts should be between
    # Ideally they should be generally in the 1850 to 2050 space
    print(op, counts[op], 1850 < counts[op] < 2150)
