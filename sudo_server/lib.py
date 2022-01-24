import os
import pickle as p

class server:
    def __init__(self):
        self.machs = [
                machine("thor",60),
                machine("c34",60),
                machine("c33",60),
                ]

    def machs_are_available(self,chk_ms):
        for cm in chk_ms:           # check machines
            for mm in self.machs:   # my    machines
                if cm.name == mm.name and mm.reserved != 0:
                        return False
        return True

    def reserve_machines(self,chk_ms):
        astr = ''
        # reserve all machines in chk_ms
        for mm in self.machs:   # my    machines
            c = '_'
            hit = False
            for cm in chk_ms:           # check machines
                if cm.name == mm.name:
                    mm.reserved = 1 
                    hit = True
            if hit:
                c = '*'
            astr += f'{c}'
        astr.rstrip()
        return f'{astr}'

    def release_machines(self,chk_ms):
        astr = ''
        # release all machines in chk_ms
        for mm in self.machs:   # my    machines
            c = '_'
            hit = False
            for cm in chk_ms:           # check machines
                if cm.name == mm.name:
                    mm.reserved = 0 
                    hit = True
            if hit:
                c = '*'
            astr += f'{c}'
        astr.rstrip()
        return f'{astr}'

    def __str__(self):
        astr = ''
        for m in self.machs:
            c = '_'
            if m.reserved == 1:
                c = '*'
            astr += f'{c}'

        astr.rstrip()
        return f'{astr}'


class machine:
    def __init__(self,name,cores):
        self.name = name
        self.cores = cores
        self.reserved = 0

    def __str__(self):
        return f'{self.name}:{self.cores} r[{self.reserved}]'

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

    def print_machines(self):
            astr = ''
            for m in self.machines:
                astr += f'{m}' + ' '
    
            astr.rstrip()
            return f'{astr}'

    def print_mnames(self):
            astr = ''
            for m in self.machines:
                astr += f'{m.name}' + ' '
    
            astr.rstrip()
            return f'{astr}'

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

        return r_new# }}}


