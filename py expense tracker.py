import pandas as pd
import matplotlib.pyplot as plt

print("####  #   #    ##### #   # ####  ##### #   #  ###  #####    ##### ####   ###   ###  #   # ##### ####  ")
print("#   #  # #     #      # #  #   # #     ##  # #     #          #   #   # #   # #     #  #  #     #   # ") 
print("####    #      ####    #   ####  ####  # # # #     ####       #   ####  ##### #     ###   ####  ####  ") 
print("#       #      #      # #  #     #     #  ## #     #          #   #  #  #   # #     #  #  #     #  #  ")
print("#       #      ##### #   # #     ##### #   #  ###  #####      #   #   # #   #  ###  #   # ##### #   # ")
print("")
print("IMPORTANT INSTRUCTION: CSV files must be named using the format 'monthN'")
print("(e.g., 'month1' for January, 'month2' for February, ... 'month12' for December")
print("")
print("")
 
#months in year 1
month1= pd.read_csv('month1.csv',index_col=0)
month2= pd.read_csv('month2.csv',index_col=0)
month3= pd.read_csv('month3.csv',index_col=0)
month4= pd.read_csv('month4.csv',index_col=0)
month5= pd.read_csv('month5.csv',index_col=0)
month6= pd.read_csv('month6.csv',index_col=0)
month7= pd.read_csv('month7.csv',index_col=0)
month8= pd.read_csv('month8.csv',index_col=0)
month9= pd.read_csv('month9.csv',index_col=0)
month10= pd.read_csv('month10.csv',index_col=0)
month11= pd.read_csv('month11.csv',index_col=0)
month12= pd.read_csv('month12.csv',index_col=0)


#To display the expense contribution of each week in a month
a=input("Please enter a month to know the contribution of each week in a month: ")
if a=="january":
    w1=month1["week1"].sum()
    w2=month1["week2"].sum()
    w3=month1["week3"].sum()
    w4=month1["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in january")
    plt.show()

elif a=="february":
    w1=month2["week1"].sum()
    w2=month2["week2"].sum()
    w3=month2["week3"].sum()
    w4=month2["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in february")
    plt.show()

elif a=="march":
    w1=month3["week1"].sum()
    w2=month3["week2"].sum()
    w3=month3["week3"].sum()
    w4=month3["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in march")
    plt.show()

elif a=="april":
    w1=month4["week1"].sum()
    w2=month4["week2"].sum()
    w3=month4["week3"].sum()
    w4=month4["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in april")
    plt.show()

elif a=="may":
    w1=month5["week1"].sum()
    w2=month5["week2"].sum()
    w3=month5["week3"].sum()
    w4=month5["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in may")
    plt.show()

elif a=="june":
    w1=month6["week1"].sum()
    w2=month6["week2"].sum()
    w3=month6["week3"].sum()
    w4=month6["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in june")
    plt.show()

elif a=="july":
    w1=month7["week1"].sum()
    w2=month7["week2"].sum()
    w3=month7["week3"].sum()
    w4=month7["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in july")
    plt.show()

elif a=="august":
    w1=month8["week1"].sum()
    w2=month8["week2"].sum()
    w3=month8["week3"].sum()
    w4=month8["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in august")
    plt.show()

elif a=="september":
    w1=month9["week1"].sum()
    w2=month9["week2"].sum()
    w3=month9["week3"].sum()
    w4=month9["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in september")
    plt.show()

elif a=="october":
    w1=month10["week1"].sum()
    w2=month10["week2"].sum()
    w3=month10["week3"].sum()
    w4=month10["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in october")
    plt.show()

elif a=="november":
    w1=month11["week1"].sum()
    w2=month11["week2"].sum()
    w3=month11["week3"].sum()
    w4=month11["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in november")
    plt.show()

elif a=="december":
    w1=month12["week1"].sum()
    w2=month12["week2"].sum()
    w3=month12["week3"].sum()
    w4=month12["week4"].sum()
    s=[w1,w2,w3,w4]
    weeks=['Week 1', 'Week 2', 'Week 3', 'Week 4']
    plt.pie(s,labels=weeks,autopct='%1.1f%%')
    plt.title("Expense of each week in december")
    plt.show()

else:
    print("sorry wrong input! ")

print("")
print("")

#To analyse the trend of expense over the weeks in a month (eg:in april)
b=input("please enter a month to analyse the trend of expense over the weeks in a month: ")

if b=="january":
    plt.plot(month1, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in january")
    plt.legend(month4)
    plt.show()

elif b=="february":
    plt.plot(month2, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in february")
    plt.legend(month4)
    plt.show()

elif b=="march":
    plt.plot(month3, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in march")
    plt.legend(month4)
    plt.show()

elif b=="april":
    plt.plot(month4, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in april")
    plt.legend(month4)
    plt.show()

elif b=="may":
    plt.plot(month5, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in may")
    plt.legend(month4)
    plt.show()

elif b=="june":
    plt.plot(month6, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in june")
    plt.legend(month4)
    plt.show()

elif b=="july":
    plt.plot(month7, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in july")
    plt.legend(month4)
    plt.show()

elif b=="august":
    plt.plot(month8, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in august")
    plt.legend(month4)
    plt.show()

elif b=="september":
    plt.plot(month9, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in september")
    plt.legend(month4)
    plt.show()

elif b=="october":
    plt.plot(month10, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in october")
    plt.legend(month4)
    plt.show()

elif b=="november":
    plt.plot(month11, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in november")
    plt.legend(month4)
    plt.show()

elif b=="december":
    plt.plot(month12, marker='o')
    plt.xlabel("Week")
    plt.ylabel("Expenses")
    plt.title("Analyisis of expense in december")
    plt.legend(month4)
    plt.show()

else:
    print("sorry wrong input! ")
    
print("")
print("")

#To display totlal expense of each month in a year
m1=month1.values.sum()
m2=month2.values.sum()
m3=month3.values.sum()
m4=month4.values.sum()
m5=month5.values.sum()
m6=month6.values.sum()
m7=month7.values.sum()
m8=month8.values.sum()
m9=month9.values.sum()
m10=month10.values.sum()
m11=month11.values.sum()
m12=month12.values.sum()
y1values=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
y1months=["january","february","march","april","may","june","july",
          "august","september","october","november","december"]
plt.bar(y1months,y1values,color="lightgreen",edgecolor="black")
plt.xlabel("Expenses")
plt.title("monthly Expenses of year1")
plt.show()
