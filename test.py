from main import *
from time import sleep as s

def clear(line_count):
    sys.stdout.write("\033[F\033[K" * line_count)
    sys.stdout.flush()

for i in range(100, 0, -1):
    clear(1)
    print(i)
    s(0.2)

