

## function to optimize
z = lambda x1 , x2 , x3 , x4 , x5: 7*x1 + 14*x2 + 6*x3 + 10*x4 - 3*x5

#constraints:
# con_1 = lambda x1 , x2 , x3, x4, x5 : x1 + x2 - 3*x5 == x3 + x4 - 4*x5
con_1 = lambda x1 , x2 , x5 : x1 + x2 == 3*x5
con_2 = lambda x2 , x4 , x5      : 3*x2   + 2*x4 + x5 <= 6000
con_3 = lambda x5 : x5  <= 4000
con_4 = lambda x3 , x4 , x5 : x3 + x4 == 4*x5

import random
import pandas as pd

def simulate (iterations = 10000000):   #using pandas
    data = []
    for i in range(iterations):
        x1 = random.randint(0 , 12000)
        x2 = random.randint(0 , 12000)
        x3 = random.randint(0 , 16000)
        x4 = random.randint(0 , 16000)
        x5 = random.randint(0 , 4000)
        if ( con_1 (x1 , x2 , x3) and
             con_2 (x2 , x4 , x5 ) and
             con_3 (x5) and
             con_4 (x3 , x4 , x5)
           ):
             #print (z(x1 , x2 , x3 , x4))
             data.append([z(x1 , x2 , x3 , x4 , x5) , x1 , x2 , x3 , x4 , x5])
        # else:
            # print ('failed: ', 'con_1 = ', con_1 (x , y) , 'con_2 = ' , con_2 (x , y) ,
            #                    'con_3 = ' , con_3(x), 'con_4 = ', con_4(y) , 'x = ' , x , 'y = ', y)
    results = pd.DataFrame(data , columns=['z', 'x1', 'x2', 'x3', 'x4' , 'x5'])
    #print (results)
    # print ('minimum found : ' , results.z.min())
    # print (results[results.z == results.z.min()])
    print ('max found : ' , results.z.max())
    print (results[results.z == results.z.max()])

#running it
for i in range (100):
    simulate()
