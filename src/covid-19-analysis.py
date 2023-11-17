# -*- coding: utf-8 -*-
#import and collecting data-Set:
#https://data.gov.in/major-indicator/covid-19-india-data-source-mohfw
import xlrd
book = xlrd.open_workbook('C:/Users/Aadi/Desktop/Sample.xlsx')
sheet = book.sheet_by_name('Sheet1')
positive = [sheet.cell_value(r, 0) for r in range(sheet.nrows)]
recovery = [sheet.cell_value(r, 1) for r in range(sheet.nrows)]
death = [sheet.cell_value(r, 2) for r in range(sheet.nrows)]
#Binary Index Tree

def getsum(BITTree,i):
 s = 0
 i = i+1
 while i > 0:
    s += BITTree[i]
    i -= i & (-i)
 return s
 
def updatebit(BITTree , n , i ,v):
 i += 1
 while i <= n:
    BITTree[i] += v
    i += i & (-i)
 
def construct(arr, n):
 BITTree = [0]*(n+1)
 
 for i in range(n):
    updatebit(BITTree, n, i, arr[i])
    return BITTree
BITTree_positive = construct(positive,len(positive));
BITTree_recovery = construct(recovery,len(recovery));
BITTree_death = construct(death,len(death));
#construct cumulative sum:
c_positive = [];
c_recovery =[];
c_death =[];
for i in range(len(positive)):
 c_positive.append(getsum(BITTree_positive,i));
 c_recovery.append(getsum(BITTree_recovery,i));
 c_death.append(getsum(BITTree_death,i));
#plot cumulative graph:
import matplotlib.pyplot as plt
plt.plot(c_positive ,color = 'y', marker = '.' , label = "Patients Covid Positive");
plt.plot(c_recovery , color = 'g', marker = '.',label = 'Pattient Recovery');
plt.plot(c_death , color = 'r', marker = '.',label = 'Pattient death');
plt.xlabel("Cumulative States")
plt.ylabel("Number of Patients")
plt.legend();
plt.grid();
plt.show();
