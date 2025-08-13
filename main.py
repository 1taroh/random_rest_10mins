import csv
import random
import itertools
from tqdm import tqdm
import time

with open("rest.csv") as f:
    reader = csv.reader(f)
    rest_list = [row for row in reader]
    rest_list = list(itertools.chain.from_iterable(rest_list))
    random.shuffle(rest_list)
    print(rest_list[0])

total_seconds = 10 * 60 # [s]
# total_seconds = 10 # [s]
print("start!")
for i in tqdm(range(total_seconds)):
    time.sleep(1)

print("done!")
