import concurrent.futures
import time
from lib import *
import threading

cv = threading.Condition()
rs = runSet()

def fake_run(run):
    for i in range(10):
        astr = '.'*i
        print(f'* [{run.number}] FAKERUN {run} [{astr}]')
        time.sleep(1)

def run_sim(run):

    cv.acquire()
    while not rs.machs_are_available(run.machines):
        time.sleep(5)
        cv.wait()
    rs.reserve_machines(run.machines,run.number)
    cv.notify()
    cv.release()

    fake_run(run)
    #print(f'run {num} working... {run}')
    #time.sleep(10)
    cv.acquire()
    rs.release_machines(run.machines)
    cv.notify()
    cv.release()
    return f'done run #{run.number}'

future_to_run = dict()
try:
    while(True):


        runs = rs.watch()

        if len(runs) > 0:
            print('new runs:')
            print_runs(runs)

            print('all runs:')
            print_runs(rs.runs)

            with concurrent.futures.ThreadPoolExecutor() as executor:
                for run in runs:
                    f = executor.submit(run_sim, run)
                    future_to_run[f] = run 

        time.sleep(5)
except:
    print()
    for f in concurrent.futures.as_completed(future_to_run):
        print(f.result())




