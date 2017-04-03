

## function to optimize f(x,y) = 30x + 40y
f = lambda x , y : 30 * x + 40 * y

#constraints:
# 20x + 30y ≥ 3 000
# 40x + 30y ≥ 4 000
con_1 = lambda x , y : 20 * x + 30 * y >= 3000
con_2 = lambda x , y : 40 * x + 30 * y >= 4000

import random
import pandas as pd

## This is a very informative function, prints on screen to appreciate teh results.
def simulate (iterations = 50000):
    possible_results = []
    for i in range(iterations):
        x = random.randint(0 , 100)
        y = random.randint(0 , 100)
        if ( con_1 (x , y) and
             con_2 (x , y)):
             print (f(x , y))
             possible_results.append(f(x , y))
        else:
            print ('value does not meet constraints')
            print ('x = ' , x , 'y = ', y)
            print ('con_1 = ', con_1 (x , y) , 'con_2 = ' , con_2 (x , y))
    print (possible_results)
    print (min(possible_results))

def simulate2 (iterations = 50000):
    data = []
    for i in range(iterations):
        x = random.randint(0 , 100)
        y = random.randint(0 , 100)
        if ( con_1 (x , y) and
             con_2 (x , y)):
             print (f(x , y))
             data.append([f(x , y) , x , y])
        else:
            print ('value does not meet constraints')
            print ('x = ' , x , 'y = ', y)
            print ('con_1 = ', con_1 (x , y) , 'con_2 = ' , con_2 (x , y))
    results = pd.DataFrame(data , columns=['f', 'x', 'y'])
    print (results)
    print (results.f.min())
    print (results[results.f == results.f.min()])
    # print (min(possible_results))

#running it
# simulate()
simulate2()
