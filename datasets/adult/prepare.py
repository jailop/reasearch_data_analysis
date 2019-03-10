import pandas as pd

data = pd.read_csv('adult.data', header=None)
data.columns = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 
        'marital-status', 'occupation', 'relationship', 'race', 'sex', 
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
        'label'
    ]
data.to_csv('adult.csv', index=False)
