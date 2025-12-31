# Sports Reference App
Converting JSON win-loss data for mlb teams

## Solution
This solution implements a simple object oriented approach to converting the input data into a pandas DataFrame which is then cleaned up into a table (still of type DataFrame) showing each teams wins and losses

## Steps
### 1: Load the contents a json file into memory and convert to a python json type. 
This is implemented in the JsonLoader class. The contents of the file are cleaned of leading and trailing newline characters, and single quotes are replaced with double quotes as double quotes are the standard for JSONs.


### 2: Convert the json into a pandas DataFrame.
This is done easily with pandas built in loading methods. pd.DataFrame.from_dict works well with json structured data.

### 3. Create an example table for viewing from the DataFrame.
By sorting the rows and columns and then displaying only the wins for each team, we create a preliminary example of a table ready for a user to view.

## Example Output
|     | BRO | BSN | CHC | CIN | NYG | PHI | PIT | STL |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| BRO | --  | 10  | 15  | 15  | 14  | 14  | 15  | 11  |
| BSN | 12  | --  | 13  | 13  | 13  | 14  | 12  | 9   |
| CHC | 7   | 9   | --  | 12  | 7   | 16  | 8   | 10  |
| CIN | 7   | 9   | 10  | --  | 13  | 13  | 13  | 8   |
| NYG | 8   | 9   | 15  | 9   | --  | 12  | 15  | 13  |
| PHI | 8   | 8   | 6   | 9   | 10  | --  | 13  | 8   |
| PIT | 7   | 10  | 14  | 9   | 7   | 9   | --  | 6   |
| STL | 11  | 13  | 12  | 14  | 9   | 14  | 16  | --  |


## Actual Output:
```
Error loading JSON. Replacing ' single quotes with double per json standard format
      BRO   BSN   CHC   CIN   NYG   PHI   PIT   STL
BRO   NaN  12.0   7.0   7.0   8.0   8.0   7.0  11.0
BSN  10.0   NaN   9.0   9.0   9.0   8.0  10.0  13.0
CHC  15.0  13.0   NaN  10.0  15.0   6.0  14.0  12.0
CIN  15.0  13.0  12.0   NaN   9.0   9.0   9.0  14.0
NYG  14.0  13.0   7.0  13.0   NaN  10.0   7.0   9.0
PHI  14.0  14.0  16.0  13.0  12.0   NaN   9.0  14.0
PIT  15.0  12.0   8.0  13.0  15.0  13.0   NaN  16.0
STL  11.0   9.0  10.0   8.0  13.0   8.0   6.0   NaN
```
