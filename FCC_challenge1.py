import numpy as np

#Author: Ardit Koti
# Calculator for mean, var, std, etc., using numpy.

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        mtx = np.array(list).reshape(3,3)
        calculations = {}
        # [Axis 1, Axis 2, Flattened]
        mean = [(mtx.mean(axis=0).tolist()), (mtx.mean(axis=1).tolist()),
            (mtx.flatten().mean())]

        var = [(mtx.var(axis=0).tolist()), (mtx.var(axis=1).tolist()),
           (mtx.flatten().var())]

        std = [(mtx.std(axis=0).tolist()), (mtx.std(axis=1).tolist()),
           (mtx.flatten().std())]

        max = [(mtx.max(axis=0).tolist()), (mtx.max(axis=1).tolist()),
           (mtx.flatten().max())]

        min = [(mtx.min(axis=0).tolist()), (mtx.min(axis=1).tolist()),
           (mtx.flatten().min())]

        sum = [(mtx.sum(axis=0).tolist()), (mtx.sum(axis=1).tolist()),
           (mtx.flatten().sum())]

        calculations['mean'] = mean
        calculations['variance'] = var
        calculations['standard deviation'] = std
        calculations['max'] = max
        calculations['min'] = min
        calculations['sum'] = sum
        return calculations