# py-expense-tracker
this was my school project, and the conditions were we could only use python and csv to make a expense tracker.
And this is a simple Python command-line tool that reads a year's worth of monthly expense data from CSV files and visualizes it with pandas and matplotlib.
![image](https://github.com/aadidevbenny1/py-expense-tracker/blob/2750402d287702677991bf4f1e72b8565e591e37/Screenshot%202026-09-05%20024737.png)

## What it does
so bascically a person/business can save their daily expenses in excel and this python program will give insight and patters of expenses for you.

The script runs three analyses in sequence:

1. **Weekly contribution pie chart** — Prompts for a month name and shows a
   pie chart of how much each week (`week1`–`week4`) contributed to that
   month's total expenses.
   ![image alt](https://github.com/aadidevbenny1/py-expense-tracker/blob/2750402d287702677991bf4f1e72b8565e591e37/Screenshot%202025-10-07%20170320.png)
   
3. **Weekly trend line chart** — Prompts for a month name and plots a line
   chart of expenses across the weeks/columns in that month's data, to show
   the trend over time.
   ![image alt](https://github.com/aadidevbenny1/py-expense-tracker/blob/2750402d287702677991bf4f1e72b8565e591e37/Screenshot%202025-10-07%20170338.png)
   
5. **Yearly bar chart** — Automatically generates a bar chart comparing the
   total expenses of all 12 months in the year, no input required.
   ![image alt](https://github.com/aadidevbenny1/py-expense-tracker/blob/2750402d287702677991bf4f1e72b8565e591e37/Screenshot%202025-10-07%20170352.png)

## Requirements

- Python 3
- `pandas`
- `matplotlib`

Install dependencies with:

```bash
pip install pandas matplotlib
```

## Input file format

The script expects **12 CSV files in the same directory** as the script,
named exactly:

```
month1.csv
month2.csv
month3.csv
...
month12.csv
```

Where `month1` = January, `month2` = February, and so on through `month12` =
December.

Each CSV must have:
- An index column in the **first column**.
- Columns named `week1`, `week2`, `week3`, `week4` containing numeric expense
  amounts for that week.

Example (`month1.csv`):
![image alt](https://github.com/aadidevbenny1/py-expense-tracker/blob/2750402d287702677991bf4f1e72b8565e591e37/Screenshot%202025-10-07%20170425.png)

```

## Usage

1. Place `month1.csv` through `month12.csv` in the same folder as the script.
2. Run the script:

   ```bash
   python py_expense_tracker.py
   ```

3. When prompted **"Please enter a month to know the contribution of each
   week in a month"**, type a full month name in lowercase (e.g. `january`).
   A pie chart window will open — close it to continue.
4. When prompted **"please enter a month to analyse the trend of expense
   over the weeks in a month"**, type a full month name in lowercase again.
   A line chart window will open — close it to continue.
5. The script then automatically displays a bar chart of total expenses for
   all 12 months.

## Notes and known limitations

Al this limitations are due the project condtions and my time restrains, you can improve this project. and if you have any doubts you can ask me I'll help you when I am free.
   
- **Month names must be lowercase and fully spelled out** (e.g. `january`,
  not `Jan` or `January`). Any other input prints `sorry wrong input!` and
  skips that chart.
- **All 12 CSV files must exist** at startup — the script reads all of them
  upfront, so it will crash with a `FileNotFoundError` if even one file
  (e.g. `month12.csv`) is missing, even if you only want to analyze one
  month.
- The trend chart's `plt.legend(...)` call always references `month4`
  regardless of which month was selected 
- Each chart call blocks execution until you close the chart window
  (`plt.show()` is blocking by default).
- The script only supports a single year of data (`month1`–`month12`); it
  has no concept of multiple years.
