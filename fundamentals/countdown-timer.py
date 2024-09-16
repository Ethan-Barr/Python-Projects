import time

set_time = int(input('How long do you want the timer for in seconds: '))


for i in range(set_time):
    print(f'\rCountdown: {set_time - i} seconds remaining               ', end='') # extra space to allow for line to be properly cleared upon refresh
    time.sleep(1)

print('\rCountdown: 0 seconds remaining')
print("Timer completed \n")




# Extension (optional)
# Add a progress bar using the 'tqdm' module 

from tqdm import tqdm
 
for i in tqdm (range (set_time, 0, -1), desc="Timer"):
    time.sleep(1)
    pass

print("Timer completed")