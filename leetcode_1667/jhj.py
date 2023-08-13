import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    users.sort_values(by='user_id',inplace=True)

    return users

"""
Runtime: 271 ms
Memory Usage: 61.4 MB
"""