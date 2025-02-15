import pandas as pd
import numpy as np

# Create a dataframe with 10 rows and 4 columns filled with random values
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])

# Highlight the 'A' and 'C' columns with different colors
def highlight_columns(val):
    color = 'yellow' if val.name == 'A' else 'lightgreen' if val.name == 'C' else ''
    return f'background-color: {color}'

# Apply the highlight function to the dataframe
styled_df = df.style.applymap(highlight_columns)

styled_df