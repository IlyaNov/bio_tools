import numpy as np 
import pandas as pd
import pyabf

def __generate_table(amount, max_epochs):
    return pd.DataFrame(data=[[np.NaN for i in range(max_epochs)] for i in range(amount)])

def generate_tables(experiments,amount, max_epochs,min_,max_,):
    table_I = __generate_table(amount, max_epochs)
    table_V = __generate_table(amount, max_epochs)
    indexes_names = []
    indexes_epochs = []
    indexes_square = []

    for exp_n, exp in enumerate(experiments):
        abf = pyabf.ABF(f'data/{exp}.abf')
        indexes_names.append(abf.abfID)
        epochs = min(experiments[exp]['epochs'],abf.sweepCount)
        indexes_epochs.append(epochs)

        square = experiments[exp]['square']
        indexes_square.append(square)

        sweep_points = abf.sweepPointCount
        for epoch in range(epochs):
            I = abf.data[1][epoch*sweep_points:(1+epoch)*sweep_points][min_:max_].mean() / square
            V = abf.data[0][epoch*sweep_points:(1+epoch)*sweep_points][min_:max_].mean()
            table_I.loc[exp_n,epoch] = I / 1000_000_000
            table_V.loc[exp_n,epoch] = V
    
    description = pd.DataFrame(data = {
        'names':indexes_names,
        'epochs':indexes_epochs,
        'square':indexes_square,

    })
    table_I = description.join(table_I)
    table_V = description.join(table_V)

    return table_I, table_V
    
def statistics_calc(table_I, table_V):
    columns = [column for column in table_I.columns.tolist() if column not in ['names','epochs','square']]
    table_I = table_I[columns]
    table_V = table_V[columns]
    V_means = table_V.mean().values
    V_sem = table_V.sem().values

    I_means = table_I.mean().values
    I_sem = table_I.sem().values

    return pd.DataFrame(data={
        'V_means' : V_means,
        'V_sem' : V_sem,
        'I_means' : I_means,
        'I_sem' : I_sem,
    })

