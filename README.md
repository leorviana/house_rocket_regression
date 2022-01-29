# House Rocket - Parte II
A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia.

Sua principal estratégia é comprar boas casas em ótimas localizações com preços baixos e depois revendê-las posteriormente à preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e portanto maior sua receita.
<p align="center">
  <img src="https://imgix.cosmicjs.com/b8301210-f45f-11ea-8507-71ed316973d3-How-to-Find-Out-How-Much-a-House-Sold-For.png">
</p>

# Problema de Negócio
A empresa obteve bons retornos com a estratégia anterior de comprar apartamentos que estivessem sendo vendidos a um valor abaixo da média da sua região. Mas o CEO da House Rocket gostaria de maximizar ainda mais os lucros.

Como cientistas de dados responsáveis por solucionar este problema, a melhor solução para uma segunda iteração do projeto é desenvolver um modelo de precificação.

# Planejamento

## Proposta
O CEO da House Rocket gostaria de maximizar ainda mais os lucros após a primeira iteração do projeto.

Com isso, uma boa estratégia é fornecer à equipe de pesquisa e ao CEO um modelo de precificação em produção que irá receber um vetor de características de um imóvel e irá retornar o valor estimado para o mesmo.

Assim, a equipe poderá identificar boas oportunidades de imóveis que estão abaixo do preço normalmente estimado pelo mercado.

## Utilização do Modelo
A equipe de pesquisa de imóveis podera consultar o modelo via API. Assim a equipe irá passar um vetor de características (ou uma matriz, caso seja avaliado varios imóveis de uma vez) e o modelo irá retornar o valor estimado para o(s) imóvel, assim poderão comparar o valor estimado pelo modelo com o real valor pedido pelo imóvel e estimar se é uma boa oportunidade de negócio.

## Vantagens e Desvantagens
### Vantagens
Basicamente, modelos de precificação economizam tempo, dinheiro e esforço. Eles podem fazer vários cálculos e comparações em segundos e não precisam sair fisicamente para ver uma propriedade ou propriedades semelhantes. Tudo isso reduz o custo de avaliar uma propriedade ou várias propriedades. Além de serem mais baratos e mais rápidos, os algoritmos não estão sujeitos a erro humano – ou má conduta. Como são autômatos, eles removem o preconceito e a subjetividade da equação. Portanto, há menos risco de fraude ou erro deliberado.

### Desvantagens
Para um modelo de precificação funcionar bem, ele precisa de dados de alta qualidade em quantidade suficiente para ser representativo. É aí que reside sua vulnerabilidade.
Caso haja escassez de imóveis comparáveis ou dados registrados também podemos ter um problema. Por esta razão, propriedades recém-construídas são especialmente difíceis de avaliar.
E por fim, um modelo de precificação só pode trabalhar com os dados que lhe são fornecidos, e há sempre o perigo de os dados serem inseridos incorretamente. Além disso, as informações que ele possui podem não estar atualizadas, tornando-o não confiável em mercados imobiliários em rápida mudança.


## Sobre o Modelo
 
### Tipo de Modelo
Modelo de Regressão em batch que precifica imóveis a partir de suas características.
 
### Disponibilização
O modelo será disponibilizado via API.

### Dados disponíveis
Os dados disponíveis estãp em um arquivo csv disponibilizado pela empresa.

### Features usadas pelo modelo

- N° de quartos
- N° de banheiros
- Ft² da casa
- N° de andares
- Nível da vista
- Nível de Design
- Latitude
- Ft² médio do interior dos 15 imóveis vizinhos

### Manutenção
O modelo deverá ser treinado a cada 15 dias com novos dados, para assim acompanhar as mudanças no mercado e não perder sua acertibilidade.

# Modelagem

## Outliers
Para identificar os outliers, utilizei o conceito de limite inferior e limite superior aplicado por gráficos de caixa(boxplot). Decidi ser um pouco agressivo e remover todos os outliers, pois haviam muitos extremos, interferindo de maneira grave na distribuição da variável resposta.

## Selecão de Variáveis
Após olhar para a correlação entre as variáveis, foram selecionadas 8.
<p align="left">
  <img src="">
</p>

## Normalizando as variáveis
Nós temos que colocar as veriáveis em uma mesma escala para que o modelo não trate uma ou outra com maior importância. Nós escolhemos normalizar os dados invés de padronizar pois as variáveis seguem uma distribuição não normal, em casos assim Normalizar, ou seja, escalonar os dados para que fiquem em um intervalo de 0 e 1, não distorce o fenômeno.

## Hold-out e Validação Cruzada
Separamos os dados em 80% treino e 20% teste, mas os dados de teste só serão utilizados no final de todo o processo para avaliar a capacidade de generalização em dados não vistos, para escolher o melhor modelo e os melhores hiperparâmetros será usada a validação cruzada.

## Treinamento
Foram treinados e testados em validação cruzada 4 modelos diferentes.
1. Regressão Linear
2. Regressão Polinomial de grau 3
3. Random Forest
4. Gradient Boosting

A melhor performance com menor sobreajuste foi o algorítimo de Gradient Boosting. Com uma performance em validação cruzada de:
- R2: 0.80
- Mape: 0.14
- RMSE: 85146.28

## Otimização de Hiperparâmetros
Usando o Randomized Search que consiste em uma busca aleatória para identificar o melhor grupo de parâmetros em um conjunto. Com isso conseguimos melhorar um pouco a performance do modelo.
- R2: 0.81
- Mape: 0.13
- RMSE: 82380.62

## Avaliação Final

Finalmente, agora para avaliar a capacidade de generalização do modelo, vamos utiliza-lo nos dados de teste que deixamos separados. Sua perfomance foi de:
- R2: 0.82
- Mape: 0.13
- RMSE: 80079.49

Temos praticamente a mesma performance que obtivemos nos dados de treino e na validação cruzada, isto significa que nosso modelo está generalizando muito bem, com pouco ou nenhum sobreajuste.

## Deploy em Produção
Para disponilizar o modelo foi utilizado o app Streamlit, que nos possibilita a criação de um web app para fornecer as previsões. O modelo pode ser acessado e utilizado através do link abaixo:

<https://share.streamlit.io/leorviana/house_rocket_regression/main/handler.py>

## Riscos Assumidos
1. Removi todos os outliers, com isso posso ter pedido informações significantes, vale realizar uma análise somente desses dados posteriormente.
2. Algumas variáveis estão bem desbalanceadas, como "waterfront" e "view", talvez se aplicarmos um método de sobreamostragem o modelo poderia performar bem melhor.
3. Ao construir um modelo de regressão é importante que a variável resposta e as variáveis explicativas estejam em uma distribuição normal para melhor performance do modelo, mas nesta primeira iteração do projeto eu não transformei a distribuição e isso pode ter afetado o desempenho de alguma maneira.

# Performance de Negócio


# Conclusão

# Próximos Passos
1. Coletar mais dados, mais em quantidade e mais atibutos, para aumentar a acertibilidade do modelo.
2. Realizar uma segunda iteração deste projeto, mas desta vez balanceando algumas variáveis, transformando a distribuição e testar modelos mais complexos.

# Referências
Blog “Seja um DataScientist - Meigarom”. Disponível em: <https://sejaumdatascientist.com/>.
 "Machine Learning Canvas", ownml. Disponível em: <https://www.ownml.co/machine-learning-canvas>.
