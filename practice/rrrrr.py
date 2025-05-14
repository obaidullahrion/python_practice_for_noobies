
import time
import sys

done = 'false'
def animate():
    i = 0
    for i in range(100):
        sys.stdout.write('Hacking NASA')
        time.sleep(0.1)
        sys.stdout.write(i)
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\rNASA HAS BEEN HACKED BY NASA HOGAR')

animate()
#long process here
done = 'false'