# -*- coding: utf-8 -*-
"""Data Exploration Pandas College Major.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/160ONx2ejEtN__MILI_PnOxFQ9fLIi4-w
"""

import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
df.head()

df.shape

df.columns

df.isna()

df.tail()

clean_df = df.dropna()
clean_df.tail()

clean_df['Starting Median Salary']

clean_df['Starting Median Salary'].max()

clean_df['Starting Median Salary'].idxmax()

clean_df['Undergraduate Major'].loc[43]



"""What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience)."""

clean_df.columns

clean_df['Mid-Career Median Salary'].max()

clean_df['Mid-Career Median Salary'].idxmax()

clean_df.loc[8]

"""Which college major has the lowest starting salary and how much do graduates earn after university?

"""

clean_df['Starting Median Salary'].min()

clean_df['Starting Median Salary'].idxmin()

clean_df.loc[49]

clean_df['Mid-Career Median Salary'].loc[49]

"""Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?"""

clean_df['Mid-Career Median Salary'].idxmin()

clean_df.loc[18]

clean_df['Mid-Career 90th Percentile Salary'].loc[18]

"""Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk"""

spread_col = clean_df['Mid-Career 90th Percentile Salary']-clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1,'Spread',spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major','Spread']].head()

high_potential = clean_df.sort_values(by='Mid-Career 90th Percentile Salary',ascending=False)
high_potential[["Undergraduate Major",'Mid-Career 90th Percentile Salary']].head()

Greatest_spread = clean_df.sort_values(by='Spread',ascending=False)
Greatest_spread[['Undergraduate Major','Spread']].head()

"""Grouping and Pivoting Data"""

clean_df.groupby('Group').count()

clean_df.groupby('Group').mean()

pd.options.display.float_format = '{:,.2f}'.format