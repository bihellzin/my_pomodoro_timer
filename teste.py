import sys
import time

a = 0
for x in range (0,10):
    agora = time.asctime()
    # \r prints a carriage return first, so `b` is printed on top of the previous line.
    sys.stdout.write('\r'+agora)
    time.sleep(1)
print ('terminou')
