import time
import sys
import pydantic
import datetime

start = datetime.datetime.now()

while True:
    time.sleep(2)
    print(sys.version)
    print(pydantic.__version__)
    print(datetime.datetime.now() - start)
    print("HELLO")
