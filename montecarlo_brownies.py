
#  x1 : brownies
#  x2 : scoops of chocolate ice cream
#  x3 : bottles of cola
#  x4 : pieces of pineapple cheesecake

## function to optimize
z = lambda x1 , x2 , x3 , x4 : 0.5*x1 + 0.2*x2 + 0.3*x3 + 0.8*x4

#constraints:
con_1 = lambda x1 , x2 , x3 , x4 : 400*x1 + 200*x2 + 150*x3 +500*x4 >= 500
con_2 = lambda x1 , x2           : 3*x1   + 2*x2 >= 6
con_3 = lambda x1 , x2 , x3 , x4 : 2*x1   + 2*x2 + 4*x3 + 4*x4 >= 10
con_4 = lambda x1 , x2 , x3 , x4 : 2*x1   + 4*x2 + x3   + 5*x4 >= 8

import random
import pandas as pd

def simulate2 (iterations = 1000000):   #using pandas
    data = []
    for i in range(iterations):
        x1 = random.randint(0 , 50)
        x2 = random.randint(0 , 50)
        x3 = random.randint(0 , 50)
        x4 = random.randint(0 , 50)
        if ( con_1 (x1 , x2 , x3 , x4) and
             con_2 (x1 , x2 ) and
             con_3 (x1 , x2 , x3 , x4) and
             con_4 (x1 , x2 , x3 , x4)):
             #print (z(x1 , x2 , x3 , x4))
             data.append([z(x1 , x2 , x3 , x4) , x1 , x2 , x3 , x4])
        # else:
            # print ('failed: ', 'con_1 = ', con_1 (x , y) , 'con_2 = ' , con_2 (x , y) ,
            #                    'con_3 = ' , con_3(x), 'con_4 = ', con_4(y) , 'x = ' , x , 'y = ', y)
    results = pd.DataFrame(data , columns=['z', 'x1', 'x2', 'x3', 'x4'])
    #print (results)
    print ('minimum found : ' , results.z.min())
    print (results[results.z == results.z.min()])
    print ('max found : ' , results.z.max())
    print (results[results.z == results.z.max()])

#running it
# simulate()
simulate2()
