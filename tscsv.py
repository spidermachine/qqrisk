import tushare as ts

for str_code in ['511990']:
    df = ts.get_k_data(str_code)
    df.to_csv(str_code + ".csv")