import pandas as pd
import os

current_dir = os.getcwd()
masskill_path ='{}/data/mass_killing_offenders_public.csv'.format(current_dir)
masskill_df = pd.read_csv('masskill_path')
print(masskill_df.head())
