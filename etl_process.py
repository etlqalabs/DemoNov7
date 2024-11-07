import pandas as pd

#a )  extract process
df = pd.read_csv("employees.csv")

# b) Transformation rules

#1. Filter the data based on deptno = 10
filter_deptno = 10
filtered_df = df[df['deptno'] == filter_deptno]

#2. Convert ename to upper
filtered_df['ename']= filtered_df['ename'].str.upper().copy()

#3. Derive total salary = sal + comm and erite in to an additional column
filtered_df['total_compensation'] = filtered_df['salary']+filtered_df['commission'].fillna(0)

# c) Load the trasfromed data in to target ( csv file )
filtered_df.to_csv("tgt_employees.csv",index=False)