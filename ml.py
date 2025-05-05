import pandas as pd

# Load the data 
data = pd.read_csv('2Full_LogisticRegression2.csv')

# Count cases where Sex_F=1 and ADHD_Outcome=1
count = len(data[(data['Sex_F'] == 1.0) & (data['ADHD_Outcome'] == 1.0)])
males = len(data[(data['Sex_F'] == 0.0) & (data['ADHD_Outcome'] == 1.0)])
males_neg = len(data[(data['Sex_F'] == 1.0) & (data['ADHD_Outcome'] == 0.0)])
females = len(data[(data['Sex_F'] == 1.0) & (data['ADHD_Outcome'] == 0.0)])

print(f"Number of female participants with ADHD: {count}, {males}, {females}, {males_neg}")