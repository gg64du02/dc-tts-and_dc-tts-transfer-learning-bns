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
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(1)

    if(memoryLeft_GB < 4.):
        print("kill the ml process")
        PROCNAME = "python.exe"
        for proc in psutil.process_iter():
            # print(proc)
            if proc.name() == PROCNAME:
                print(proc)
                pid = proc.pid
                p = psutil.Process(pid)
                print(proc.memory_info()[0])
                how_much_memory_is_used = proc.memory_info()[0]
                if(proc.memory_info()[0] > 30 * 1000 * 1000):
                    print("about to kill the ml process")
                    p.terminate()  # or p.kill()


    else:
        print("nothing to kill just yet")
        # nothing to kill just yet




# virtual_memory
# print()