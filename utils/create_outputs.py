from data_classes.custom_columns import CustomColumn
import time
import pandas as pd
import os

def create_outputs(config_obj, df, mode, script_loc):
    
    all_cs_cols = config_obj.all_custom_cols

    for col_settings in all_cs_cols:
        cs_col = CustomColumn(col_settings)
        cs_col = CustomColumn.get_matches(cs_col,df)
        df[col_settings["create_col"]] = cs_col
        pass

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = script_loc + "/" + config_obj.output_folder + "/" + mode + "/" + timestamp + "/"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        pass
    
    
    df_tmp = df
    
    ## save csvs 
    try:
        df.to_csv(output_dir+"csv_plain.csv", encoding='utf-8', index=False)    
    except Exception as e:
        print('',e)
        
    try:
        df['to_mail'] = df.to_mail.apply(lambda x: str(x).split(','))
    except Exception as e:
        print('error:',e)
    
    try:
        df_exploded = df.assign(to_mail=df['to_mail']).explode('to_mail')
    except Exception as e:
        print('',e)
    
    try:
        df_exploded.to_csv(output_dir+"csv_exploded.csv", encoding='utf-8', index=False)
    except Exception as e:
        print('',e)
    
    
    
    
    print(df_tmp.head())
    df_tmp.reset_index(drop=True,inplace=True)
    pd.DataFrame.to_json(df_tmp,path_or_buf=output_dir+"json_plain.json")
    print("\n\n------")
    print(df_tmp.head())
    print("\n\n------")
    print(df_tmp["to_mail"])
    df_tmp_exploded = df_tmp.assign(to_mail=df['to_mail']).explode('to_mail')
    df_tmp.reset_index(drop=True,inplace=True)
    print("\n\n------")
    print(df_tmp.head())
    pd.DataFrame.to_json(df_tmp_exploded,path_or_buf=output_dir + "json_exploded.json",orient='records')
    
    return "Finished saving outputs."