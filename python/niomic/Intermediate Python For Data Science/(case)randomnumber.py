# # 16. Random Numbers
import numpy as np

step = 50

dice = 6

if dice <= 2:
    step -= 1
elif dice <= 5:
    step += 1
else:
    step = step + np.random.randint(1,7)

print(dice)
print(step)