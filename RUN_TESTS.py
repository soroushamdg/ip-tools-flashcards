import os
import time
print('START TEST PROCESS')

time.sleep(1)

print('START CRAWLER TEST')
time.sleep(1)
os.system(' '.join(['python','-m','unittest','crawler.TEST_CRAWLER']))

print('START DRAWER TEST')
time.sleep(1)
os.system(' '.join(['python','-m','unittest','drawer.TEST_DRAWER']))