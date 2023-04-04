import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 1882360450 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    import scipy.stats
    alpha = 1 - p
    n=len(x)
    z_m=sum(i*i for i in x)
    return np.sqrt((z_m)/(7*chi2.ppf(1-alpha/2, df=2*n))),np.sqrt((z_m)/(7*chi2.ppf(alpha/2, df=2*n))),       
