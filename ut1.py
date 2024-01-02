import unittest
import pandas as pd
import csv_to_yaml as csy
import yaml

class check(unittest.TestCase):
    def test_ans(self):
        
        df=pd.read_csv('input.csv')
        df=csy.year_month_split(df)
        year=df['Year'].unique()
        data=csy.process_year_wise(df,year)
        file=open('1.yaml','w')
        y = yaml.dump(data,file)
        with open ('check.yaml','r')as b:
            c=yaml.safe_load(b)
        self.assertAlmostEqual(data,c)

unittest.main()