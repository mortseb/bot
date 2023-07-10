from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Présumons qu'on a des données de visionnage pour quatre utilisateurs et cinq programmes.
# Chaque ligne représente un utilisateur, chaque colonne représente un programme.
# Les valeurs sont le nombre de minutes que chaque utilisateur a passé à regarder chaque programme.
data = np.array([
    [30, 30, 5, 0, 0],
    [5, 5, 30, 10, 5],
    [5, 5, 30, 10, 10],
    [20, 0, 10, 10, 5],
])

# On calcule la similarité entre les programmes.
similarity = cosine_similarity(data.T)

# Pour recommander des programmes à l'utilisateur 0, on regarde quels programmes sont les plus similaires à ceux qu'il a regardé.
user_programs = data[0, :]
similar_programs = similarity @ user_programs

# On enlève les programmes que l'utilisateur a déjà regardé.
similar_programs = similar_programs * (user_programs == 0)

# On recommande le programme le plus similaire.
recommended_program = np.argmax(similar_programs)
print(f"Programme recommandé pour l'utilisateur 0 : {recommended_program}")
