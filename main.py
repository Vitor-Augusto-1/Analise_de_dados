#importando Bibliotecas
from sys import displayhook
import pandas as pd
import plotly.express as px

# Importando os dados
tabela_cancelamentos = pd.read_csv("cancelamentos.csv")

# Exclusão de uma coluna que não iremos usar
tabela_cancelamentos = tabela_cancelamentos.drop("CustomerID", axis=1)
displayhook(tabela_cancelamentos)

# Excluindo dados nulos
displayhook(tabela_cancelamentos.info())
tabela = tabela_cancelamentos.dropna()
displayhook(tabela_cancelamentos.info())

# Format em porcentual para melhor visualização da taxa de cancelamentos
displayhook(tabela_cancelamentos['cancelou'].value_counts())
displayhook(tabela_cancelamentos['cancelou'].value_counts(normalize=True).map("{:.1%}".format))

# Cancelamento por contrato
displayhook(tabela_cancelamentos['duracao_contrato'].value_counts(normalize=True))
displayhook(tabela_cancelamentos['duracao_contrato'].value_counts())

# contratos mensais
displayhook(tabela_cancelamentos.groupby("duracao_contrato").mean(numeric_only=True))
# média de cancelamento mensal igual a 1.

#tendo em vista que o contrato mensal e ruim, vamos remover e continuar analisando.
tabela_cancelamentos = tabela_cancelamentos[tabela_cancelamentos['duracao_contrato']!="Monthly"]
displayhook(tabela_cancelamentos)
displayhook(tabela_cancelamentos['cancelou'].value_counts())
displayhook(tabela_cancelamentos['cancelou'].value_counts(normalize=True).map("{:.1%}".format))

# Verificando a quantidade de assinaturas.
displayhook(tabela_cancelamentos['assinatura'].value_counts(normalize=True))
displayhook(tabela_cancelamentos.groupby('assinatura').mean(numeric_only=True))

# Analise gráficas
for coluna in tabela_cancelamentos.columns:
        grafico = px.histogram(tabela_cancelamentos, x=coluna, color='cancelou', width=600)
        grafico.show()

# Apos visualizar os graficos encontramos alguns pontos criticos
# dias de atraso acima de 20 - 100% de cancelamento
# ligações call center acima de 5 - 100% de cancelamento

tabela_cancelamentos = tabela_cancelamentos[tabela_cancelamentos['ligacoes_callcenter']<5]
tabela_cancelamentos = tabela_cancelamentos[tabela_cancelamentos['dias_atraso']<=20]

displayhook(tabela_cancelamentos)
displayhook(tabela_cancelamentos['cancelou'].value_counts())
displayhook(tabela_cancelamentos['cancelou'].value_counts(normalize=True).map("{:.1%}".format))

# se resolvermos esse problema podemos diminuir até 26.9%
# - contrato mensal - precisamos melhorar
# - necessidades de ligações call center
# - atraso de pagamento.