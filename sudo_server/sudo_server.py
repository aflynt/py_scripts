import concurrent.futures
import time
from lib import *
import threading

cv = threading.Condition()
rs = runSet()
svr = server()

def fake_run(run):
    print(f'* [{run.number}] FAKERUN')
    time.sleep(10)

def run_sim(run):

    cv.acquire()
    while not svr.machs_are_available(run.machines):
        time.sleep(5)
        cv.wait()
    rstr = svr.reserve_machines(run.machines)
    print(f'run #{run.number} reserving {rstr} -> {svr}')
    cv.notify()
    cv.release()

    # FAKE WORK
    fake_run(run)

    cv.acquire()
    rstr = svr.release_machines(run.machines)
    print(f'run #{run.number} releasing {rstr} -> {svr}')
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




