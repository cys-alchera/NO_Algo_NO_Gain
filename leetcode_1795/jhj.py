import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(products, id_vars='product_id', var_name='store', value_name='price').dropna()

"""
Runtime: 286 ms
Memory Usage: 61.1 MB
"""