import pandas as pd
import pytest

df1 = pd.read_csv("tgt_employees.csv")

# 1. Data completeness check
def test_dataCompletenessCheck():
    assert not df1.empty,"Please check why etl job didn't load anything in target"


#2. Data Transfromation
#2.1 Filter transformation check ( deptno = 10 )
def test_dataTransfromation_FilterDeptnoCheck():
    deptno_filter = 10
    assert all(df1['deptno'] == deptno_filter),"Filter didn't work , pleae check"

#2.2 expression transformation check ( conevrsion of ename is done corectly )
def test_dataTransfromation_enameUpperCase():
    assert all(df1['ename'] == df1['ename'].str.upper()),"ename is not converted properly , please check"

#2.3 Total salary is derivered correctly
def test_dataTransformation_totalCompensation():
    calculated_total_comp = df1['salary']+df1['commission'].fillna(0)
    assert df1['total_compensation'].equals(calculated_total_comp)," total compensation derivation failed"


#3. data Quality check
def test_dataQuality():
    assert df1.isnull().sum().sum() == 0 ," There are nulls in target , please verify"