import signal
from listener import Listener
from adsb import Adsb
import sys

adsbValid = 0
adsbInvalid = 0

def handler(signum, frame):
    print(f"Valid: {adsbValid}")
    print(f"Invalid: {adsbInvalid}")
    l.stop()
    sys.exit()

# Set the signal handler
signal.signal(signal.SIGINT, handler)

adsb = Adsb()

l = Listener("adsb-monitor", 30003)
l.start()

while True:
    if l.hasData():
        squitter = l.getData()
        if adsb.isValidRec(squitter):
            adsbValid += 1
            print(f"{adsbValid}: {squitter}")
        else:
            adsbInvalid += 1

    else:
        pass

    


