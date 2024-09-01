import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("/workspaces/Wiwino_project/CSV/Wines recommended.csv")
del df['name.1']
del df['wine_name']
del df['id']
df.corr()
corr_matrix = df.corr()
corr_matrix_np = corr_matrix.values
np.fill_diagonal(corr_matrix_np, 1)
corr_matrix = pd.DataFrame(corr_matrix_np, index=corr_matrix.index, columns=corr_matrix.columns)

sns.heatmap(corr_matrix, annot=True, cmap="inferno", vmax=1, vmin=-1, fmt='.1f')
plt.title("Correlations")
plt.show()

df = pd.read_csv(r"/workspaces/Wiwino_project/CSV/Wines recommended.csv")

