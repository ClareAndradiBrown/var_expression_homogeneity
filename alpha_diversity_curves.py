import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def diversity_curve(df,sample):
    alpha_div=pd.DataFrame()
    q_list=[]
    index_list=[]
    for q in np.arange(0,3,0.01):
        if q ==1:
            continue
        else:
            count=0
            for x in df[sample]:
                x=float(x)
                x=x**q
                count=count+x
            final_d=count**(1/(1-q))
            q_list.append(q)
            index_list.append(final_d)
    alpha_div['q']=q_list
    alpha_div['div_index']=index_list
    return alpha_div
