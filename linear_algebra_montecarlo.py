

## function to optimize f(x,y) = 30x + 40y
f = lambda x , y : 30 * x + 50 * y

#constraints:
# 20x + 30y ≥ 3 000
# 40x + 30y ≥ 4 000
con_1 = lambda x , y : x + 3* y <= 200
con_2 = lambda x , y : x + y <= 100
con_3 = lambda x : x >= 20
con_4 = lambda y : y >= 10

import random
import pandas as pd

def simulate2 (iterations = 5000000):   #using pandas
    data = []
    for i in range(iterations):
        x = random.randint(19 , 1000)
        y = random.randint(9 , 1000)
        if ( con_1 (x , y) and
              con_2 (x , y) and
              con_3 (x) and
              con_4 (y)):
             print (f(x , y))
             data.append([f(x , y) , x , y])
        # else:
            # print ('failed: ', 'con_1 = ', con_1 (x , y) , 'con_2 = ' , con_2 (x , y) ,
            #                    'con_3 = ' , con_3(x), 'con_4 = ', con_4(y) , 'x = ' , x , 'y = ', y)
    results = pd.DataFrame(data , columns=['f', 'x', 'y'])
    print (results)
    print ('minimum found : ' , results.f.min())
    print (results[results.f == results.f.min()])
    print ('max found : ' , results.f.max())
    print (results[results.f == results.f.max()])

#running it
# simulate()
simulate2()
