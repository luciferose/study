from datetime import datetime
import time
import random

odds=range(1,60,2)

for x in range(5):
    right_this_minute = datetime.today().second
    print(right_this_minute)
    if right_this_minute in odds:
        print('this minute seems a little odd.')
    else:
        print('not in odds')
    x-=1
    time.sleep(random.randint(1,10))