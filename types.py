# Para verificar o type de colunas presentes nos df's podemos utlizar a função .dtypes

# Exemplo:
data_frame['coluna'].dtypes 

# ou verificar todas as colunas:
data_frame.dtypes

# Convertendo Types:
data_frame['coluna'] = pd.data_frame(data_frame['coluna']) # Converter para datetime
data_frame['coluna'] = pd.to_numeric(data_frame[ 'coluna']) # Converter para int
data_frame['coluna'] = data_frame['coluna'].astype(str) # Converter para string
data_frame['coluna'] = data_frame['coluna'].astype(int) # Converter para inteiro
