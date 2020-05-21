import psutil

import time

from datetime import datetime

currentAvailableRam_GB = 15.9

print(psutil.swap_memory().percent)
print(psutil.virtual_memory().percent)
print(psutil.virtual_memory())

percentInt = psutil.virtual_memory().percent

memoryUsed_GB = ( percentInt / 100 ) * currentAvailableRam_GB

memoryLeft_GB = float(currentAvailableRam_GB - memoryUsed_GB)
# for testing
# memoryLeft_GB = 3.

print("memoryLeft_GB",memoryLeft_GB)
print(type(memoryLeft_GB))

while True:
    if(memoryLeft_GB < 9.):
        print("kill the ml process")
        PROCNAME = "python.exe"
        for proc in psutil.process_iter():
            # print(proc)
            if proc.name() == PROCNAME:
                print(proc)
                pid = proc.pid
                p = psutil.Process(pid)
                p.terminate()  # or p.kill()
    else:
        print("nothing to kill just yet")
        # nothing to kill just yet

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        time.sleep(1)




# virtual_memory
# print()