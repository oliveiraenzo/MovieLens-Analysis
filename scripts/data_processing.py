import pandas as pd

# Etapa 1: Carregar os Dados
movies_df = pd.read_csv('data/movies.csv')
ratings_df = pd.read_csv('data/ratings.csv')
tags_df = pd.read_csv('data/tags.csv')
links_df = pd.read_csv('data/links.csv')

# Etapa 2: Limpeza dos Dados

# Renomeando colunas para simplificação
movies_df.rename(columns={'movieId': 'movie_id', 'title': 'movie_title', 'genres': 'movie_genres'}, inplace=True)
ratings_df.rename(columns={'userId': 'user_id', 'movieId': 'movie_id', 'rating': 'user_rating', 'timestamp': 'rating_timestamp'}, inplace=True)
tags_df.rename(columns={'userId': 'user_id', 'movieId': 'movie_id', 'tag': 'movie_tag', 'timestamp': 'tag_timestamp'}, inplace=True)
links_df.rename(columns={'movieId': 'movie_id', 'imdbId': 'imdb_id', 'tmdbId': 'tmdb_id'}, inplace=True)

# Remover linhas com dados faltantes
movies_df.dropna(subset=['movie_title', 'movie_genres'], inplace=True)
ratings_df.dropna(subset=['user_rating'], inplace=True)

# Remover duplicatas
movies_df.drop_duplicates(subset=['movie_id'], inplace=True)
ratings_df.drop_duplicates(subset=['movie_id', 'user_id'], inplace=True)

# Converter timestamp para formato legível (DD/MM/YYYY HH:MM:SS)
ratings_df['rating_timestamp'] = pd.to_datetime(ratings_df['rating_timestamp'], unit='s').dt.strftime('%d/%m/%Y %H:%M:%S')
tags_df['tag_timestamp'] = pd.to_datetime(tags_df['tag_timestamp'], unit='s').dt.strftime('%d/%m/%Y %H:%M:%S')

# Filtrando ratings fora da faixa de 0 a 5
ratings_df = ratings_df[(ratings_df['user_rating'] >= 0) & (ratings_df['user_rating'] <= 5)]

# Etapa 3: Análise dos Dados

# Média de avaliação por filme
avg_ratings = ratings_df.groupby('movie_id')['user_rating'].mean().reset_index()
avg_ratings.rename(columns={'user_rating': 'avg_rating'}, inplace=True)

# Número de filmes por gênero
genres_count = movies_df['movie_genres'].str.split('|', expand=True).stack().value_counts().reset_index()
genres_count.columns = ['genre', 'count']

# Número de tags por filme
tags_count = tags_df.groupby('movie_id')['movie_tag'].count().reset_index()
tags_count.rename(columns={'movie_tag': 'tags_count'}, inplace=True)

# Número de filmes com links válidos
valid_links_count = links_df.dropna(subset=['imdb_id', 'tmdb_id']).shape[0]

# Etapa 4: Exportação dos Resultados

# Salvar os dados limpos na pasta "proceeded"
movies_df.to_csv('proceeded/movies_clean.csv', index=False)
ratings_df.to_csv('proceeded/ratings_clean.csv', index=False)
tags_df.to_csv('proceeded/tags_clean.csv', index=False)
links_df.to_csv('proceeded/links_clean.csv', index=False)

# Salvar os relatórios separados por tópicos

# Relatório de Média de Avaliações por Filme
with open('proceeded/avg_ratings_report.txt', 'w') as f:
    f.write("Média de Avaliações por Filme:\n")
    f.write(avg_ratings.to_string(index=False))

# Relatório de Contagem de Filmes por Gênero
with open('proceeded/genres_count_report.txt', 'w') as f:
    f.write("Contagem de Filmes por Gênero:\n")
    f.write(genres_count.to_string(index=False))

# Relatório de Número de Tags por Filme
with open('proceeded/tags_count_report.txt', 'w') as f:
    f.write("Número de Tags por Filme:\n")
    f.write(tags_count.to_string(index=False))

# Relatório de Número de Filmes com Links Válidos
with open('proceeded/valid_links_count_report.txt', 'w') as f:
    f.write(f"Número de Filmes com Links Válidos: {valid_links_count}")
