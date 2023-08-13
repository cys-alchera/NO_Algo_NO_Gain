import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[(employees['employee_id'] % 2 == 0) | (employees['name'].str.startswith('M')),'salary'] = 0
    bonus_list = employees[['employee_id','salary']].sort_values(by='employee_id')
    bonus_list.rename(columns={'salary':'bonus'}, inplace=True)

    return bonus_list

"""
Runtime: 321 ms
Memory Usage: 61.2 MB
"""