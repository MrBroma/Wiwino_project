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


ax = sns.scatterplot(x="ratings_average", y="price_euros", data=df, color='purple', s=50, hue = 'name.1')  # Cambia 'purple' por cualquier color o paleta que desees



ax.set_title("Wine Recommendations")  
ax.set_xlabel("Average Rating")  
ax.set_ylabel("Price (Euros)")  
ax.set_xticks([4.2, 4.4, 4.6, 4.8, 5])

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8) 
plt.tight_layout()
plt.show()




