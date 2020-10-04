import os
import pickle as p

class machine:
    def __init__(self,name,cores):
        self.name = name
        self.cores = cores

    def __str__(self):
        return f'{self.name}:{self.cores}'

class run:
    def __init__(self,number,machines):
        self.number = number
        self.machines = machines

    def __str__(self):
        astr = ''
        for m in self.machines:
            astr += f'{m}' + ' '

        astr.rstrip()
        return f'{self.number}:{astr}'

def get_run_nums(runs):
    nlist = []
    for run in runs:
        nlist.append(run.number)
    return list(set(nlist))

def print_runs(runs):
    for run in runs:
        num = run.number
        machines = run.machines
        print(f'run #{num} {run}')
    print()

class runSet():
    def __init__(self):# {{{
        self.fname = "runFile"
        self.stamp = None
        self.runs = []
        self.machs = {} # mach_name, run_num

    def watch(self):
        stamp = os.stat(self.fname).st_mtime
        r_new = []
        # file changed
        if stamp != self.stamp:
            r_new = self.read_runs()
            for r in r_new:
                self.runs.append(r)

            self.stamp = os.stat(self.fname).st_mtime
        return r_new

    def read_runs(self):
    
        # read in the runs
        with open("runFile", 'rb') as f:
            runs = p.load(f)

        # find new run numbers
        n_old = get_run_nums(self.runs)
        n_in  = get_run_nums(runs)
        n_new = [x for x in n_in if x not in n_old]

        # return only new runs
        r_new = []
        for run in runs:
            n = run.number
            if n in n_new:
                r_new.append(run)

        # add machine name keys to machine dict
        for r in r_new:
            for m in r.machines:
                mname = m.name
                self.machs[mname] = 0 
    
        return r_new# }}}

    def machs_are_available(self,machines):
        for m in machines:
            mname = m.name
            if self.machs[mname] != 0:
                return False
        return True

    def reserve_machines(self,machines,num):
        for m in machines:
            mname = m.name
            self.machs[m] = num

    def release_machines(self,machines):
        for m in machines:
            mname = m.name
            self.machs[m] = 0

