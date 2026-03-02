### Analyse des résultats – Trustworthiness

La métrique de **trustworthiness** mesure à quel point la structure locale des données est préservée après réduction de dimension.  
Plus la valeur est proche de **1**, meilleure est la préservation des voisinages locaux.

#### Résultats obtenus :

- **t-SNE (0.9807)** : obtient le meilleur score et préserve très bien les relations locales entre les points.
- **UMAP (0.9728)** : offre également une excellente préservation, légèrement inférieure à t-SNE.
- **PCA (0.8715)** : est moins performant pour conserver la structure locale, ce qui est attendu car il s’agit d’une méthode linéaire.

### Conclusion

Pour la préservation des voisinages locaux, **t-SNE et UMAP sont plus adaptés que PCA** sur ce dataset.
