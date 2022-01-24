import pickle as p
from lib import *

m1  = machine("thor",60)
m2  = machine( "c34",44)
m3  = machine( "c33",44)

mlist = [m1,m2]

run1 = run(1,[m1])
run2 = run(2,[m2])
run3 = run(3,[m3])
run4 = run(4,[m1,m2,m3])
run5 = run(5,[m1])
run6 = run(6,[m1])
run7 = run(7,[m3])
run8 = run(8,[m3,m1])
run9 = run(9,[m2,m1])
run10 = run(10,[m2])

#runs = [run3]

#runs = [run1,run2, run3, run4]
runs = [
        run4,
        run2,
        run3,
        run1,
        run5,
        run6,
        run7,
        run8,
        run9,
        run10,
        ]

# write runs to file
with open("runFile", 'wb') as f:
    p.dump(runs,f)
