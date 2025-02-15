import pandas as pd
import numpy as np

# Crea un dataframe con 10 righe e 4 colonne riempito con valori casuali
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])

# Funzione per evidenziare le colonne 'A' e 'C' con colori diversi
def highlight_columns(val):
    color = 'yellow' if val.name == 'A' else 'lightgreen' if val.name == 'C' else ''
    return f'background-color: {color}'

# Applica la funzione di evidenziazione al dataframe usando map
styled_df = df.style.map(highlight_columns)

# Mostra il dataframe stilizzato
styled_df