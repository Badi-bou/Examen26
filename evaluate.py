import pandas as pd
import numpy as np
import os
from sklearn.manifold import trustworthiness
from sklearn.preprocessing import StandardScaler

# Chemins robustes
DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(DIR, 'data', 'city_lifestyle_dataset.csv')
PCA_PATH = os.path.join(DIR, 'outputs', 'pca_emb_2d.csv')
TSNE_PATH = os.path.join(DIR, 'outputs', 'tsne_emb_2d.csv')
UMAP_PATH = os.path.join(DIR, 'outputs', 'umap_emb_2d.csv')

print("Chemins:")
print(f"Data: {DATA_PATH}")
print(f"PCA: {PCA_PATH}")

if not os.path.exists(DATA_PATH):
    print("ERREUR: Dataset absent:", DATA_PATH)
    exit(1)

df = pd.read_csv(DATA_PATH)
features = ['population_density', 'avg_income', 'internet_penetration', 'air_quality_index', 
            'public_transport_score', 'green_space_ratio', 'happiness_score', 'avg_rent']
X = df[features].fillna(df[features].median())
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

files_cols = {
    PCA_PATH: ['PC1', 'PC2'],
    TSNE_PATH: ['tsne_1', 'tsne_2'], 
    UMAP_PATH: ['UMAP_1', 'UMAP_2'] 
}

results = {}
for path, cols in files_cols.items():
    if os.path.exists(path):
        df_emb = pd.read_csv(path)
        if all(col in df_emb.columns for col in cols):
            emb = df_emb[cols].values
            method = os.path.basename(path).split('_')[0].upper()
            trust = trustworthiness(X_scaled, emb, n_neighbors=5)
            results[method] = round(trust, 4)
            print(f"OK {method}: {results[method]}")
        else:
            print(f"ERREUR {os.path.basename(path)}: besoin", cols)
    else:
        print("Absent:", os.path.basename(path))

if results:
    df_results = pd.DataFrame(list(results.items()), columns=['Méthode', 'Trustworthiness'])
    df_results = df_results.sort_values('Trustworthiness', ascending=False)
    print("\nCOMPARAISON (plus haut = meilleur):")
    print(df_results.to_string(index=False))
    out_path = os.path.join(DIR, 'outputs', 'trustworthiness_results.csv')
    df_results.to_csv(out_path, index=False)
    print("Sauvé:", out_path)
else:
    print("Pas de fichiers outputs trouvés.")
