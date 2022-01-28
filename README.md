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
- RMSE: 84352.96

## Otimização de Hiperparâmetros
Usando o Randomized Search que consiste em uma busca aleatória para identificar o melhor grupo de parâmetros em um conjunto. Com isso conseguimos melhorar um pouco a performance do modelo.
- R2: 0.82
- Mape: 0.13
- RMSE: 81635.04

## Avaliação Final

Finalmente, agora para avaliar a capacidade de generalização do modelo, vamos utiliza-lo nos dados de teste que deixamos separados. Sua perfomance foi de:
- R2: 0.81
- Mape: 0.13
- RMSE: 81677.04

Temos praticamente a mesma performance que obtivemos nos dados de treino e na validação cruzada, isto significa que nosso modelo está generalizando muito bem, com pouco ou nenhum sobreajuste.

## Deploy em Produção

## Riscos Assumidos

# Performance de Negócio

# Conclusão

# Próximos Passos

# Referências
