import pandas as pd

def tuples_to_df(columns, tup):
    df = pd.DataFrame.from_records(tup,index=None,columns=columns)
    df.sort_values(["date_utc"], 
                    axis=0,
                    ascending=[True], 
                    inplace=True)
                        
    return df
