import numpy as np
import pickle
import streamlit as st
from scaler.data_prep import preprocessing


#Loading scaler
scaler = preprocessing()

#Loading model
model = pickle.load(open("model/house_sales_model.pkl", "rb"))

def main():
    st.title("Modelo de Precificação")
    c = st.container()
    n_quartos = c.slider("Número de Quartos", 0, 10)
    n_banheiros = c.slider("Número de Banheiros", 0, 10)
    n_andares = c.slider("Número de Andares", 1.0,3.0, step=0.5)
    nivel_vista = c.slider("Nível de Vista", 0, 4)
    nivel_design = c.slider("Nível de Estrutura e Design", 3, 13)
    nivel_bairro = c.slider("Nível da Vizinhança", 1, 4)
    latitude = c.number_input("Latitude em que está o imóvel", 47.0001, 47.9999)
    tamanho_imovel = c.number_input("Tamanho da construção em Ft2")
    
    entrada = np.array([n_quartos, n_banheiros, tamanho_imovel, n_andares, nivel_vista, nivel_design, latitude, nivel_bairro])
    entrada = entrada.reshape(1, -1)
    
    c2 = st.container()
    if c2.button("Precificar"):
        entrada = scaler.scaling(entrada)
        predicao = model.predict(entrada)
        predicao = predicao.round(2)
        c2.success("$ {}".format(predicao))
    
if __name__ == "__main__":
    main()