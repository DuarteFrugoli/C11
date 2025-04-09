import numpy as np

# Carregando o dataset
dataset = np.loadtxt('social_media.csv', delimiter=';', dtype=str, encoding='utf-8')

# Questão 1

# Quantidade de posts do Brasil
brasil_posts = dataset[1:, 4][dataset[1:, 4] == 'Brazil'].size

# Saída
print(f'Brasil tem {brasil_posts} posts\n')

# Questão 2

# Faz o cálculo de quantidade de hashtags education
porcentagem_hashtags_education = np.mean(dataset[1:, 2] == 'Education') * 100

# Saída
print(f'Porcentagem de hashtags education: {porcentagem_hashtags_education:.2f}%\n')

# Questão 3:

# Numpy list de trues e falses para verificar quais linhas são do instagram
instagram_mask = dataset[1:, 1] == 'Instagram'

# Médias de views e likes do insta
mean_views_instagram = np.mean(dataset[1:, 5].astype(float)[instagram_mask])
mean_likes_instagram = np.mean(dataset[1:, 6].astype(float)[instagram_mask])

# Colocando em um dicionário
dicionario_viewnlike_instagram = {'mean_views': mean_views_instagram, 'mean_likes' : mean_likes_instagram}

# Saídas
print(f'media de views no Insta: {dicionario_viewnlike_instagram['mean_views']:.0f}')
print(f'media de likes no Insta: {dicionario_viewnlike_instagram['mean_likes']:.0f}\n')

# Questão 4:

# Pegando as plataformas e a quantidade de vezes que cada uma aparece
plataformas_posts = np.unique(dataset[1:, 1], return_counts=True)
plataforma_mais_posts = plataformas_posts[0][plataformas_posts[1].argmax()] # Plataforma que mais aparece
qtd_posts = plataformas_posts[1].max() # Quantidade de posts da plataforma com mais posts

# Saída
print(f'A plataforma com a maior quantidade de posts é o {plataforma_mais_posts}, com {qtd_posts} posts\n')

# Questão 5

# Região com o post com mais likes
regiao_post_mais_likes = dataset[1:, 4][dataset[1:, 6].astype(float).argmax()]

# Quantidade de likes do post com mais likes
likes_post_mais_likes = dataset[1:, 6].astype(float).max()

# Saída
print(f'A região com o post com mais likes é o {regiao_post_mais_likes} com {likes_post_mais_likes:.0f} likes')