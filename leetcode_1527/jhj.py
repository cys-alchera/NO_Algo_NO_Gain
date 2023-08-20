import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'\bDIAB1')]

"""
Runtime: 271 ms
Memory Usage: 60.5 MB
"""