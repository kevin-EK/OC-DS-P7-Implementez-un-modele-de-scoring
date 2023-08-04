import pandas as pd
import numpy as np
import streamlit as st
import time
import requests
import joblib


MLFLOW_URI = 'http://127.0.0.1:5000/invocations'

def request_prediction(model_uri, data):
    headers = {"Content-Type": "application/json"}

    data_json = {'data': data}
    response = requests.request(
        method='POST', headers=headers, url=model_uri, json=data_json)

    if response.status_code != 200:
        raise Exception(
            "Request failed with status {}, {}".format(response.status_code, response.text))

    return response.json()


@st.cache_data
def load_data():
    important_features = joblib.load('data/cleaned/list_col_to_keep_from_train_application_final.joblib')
    data1 = pd.read_csv("data/source/application_train.csv",
                        usecols=important_features)
    data2 = pd.read_csv("data/source/application_test.csv", 
                        usecols= important_features )
    
    # Données numériques
    number_data = data1.select_dtypes(include = np.number)\
    .groupby(['TARGET']).agg(pd.Series.median).T
    
    # Données catégorielles
    categ_data_data = data1.groupby(['TARGET'])\
        .agg(pd.Series.mode)\
            .select_dtypes(exclude = np.number).T
    
    data_agg = pd.concat([number_data, categ_data_data],axis=0)
    data_agg.reset_index(inplace=True)
    data_agg.rename(columns={'index':'info', 0:'Bon', 1:'Mauvais'},inplace = True)
    data = pd.concat([data1.drop(columns = ['TARGET']), data2],axis=0).drop_duplicates()
    return data, data_agg

chosen_radio = st.sidebar.radio(
'Comment souhaitez vous entrer les valeurs du client?',("Index", "Valeur"))

if chosen_radio == "Index":
    #Chargement des données
    identifiant, data_agg = load_data()

    latest_iteration = st.empty()
    latest_iteration.write(
        "Vous identifierez le client grâce à son numéro d'identification !")
    
    #time.sleep(3)
    
    latest_iteration.markdown("## :red[Choix de l'identifiant]")
    chosen_customer = st.selectbox(
    "Quel est le numéro d'identifiant du client?", identifiant['SK_ID_CURR'])

    #'You selected: ', chosen_customer
    
    #st.table(identifiant[identifiant.SK_ID_CURR==chosen_customer])
    
    #X_data = data_agg.select_dtypes(exclude = 'object')
    #st.bar_chart(data = X_data, x='Bon', y='info')
    tab_comparaison = data_agg[['info',	'Bon', 'Mauvais']].merge(
        identifiant[identifiant.SK_ID_CURR==chosen_customer].T\
        .reset_index().rename(columns = {'index':'info', 0:'Client selectionné'}),
        on = 'info',how='inner'
                )
    st.dataframe( tab_comparaison )
    
    # Bouton Score
    predict_btn = st.sidebar.button('Obtenir le score')

    if predict_btn:
        st.balloons()
        pred = request_prediction(MLFLOW_URI, [identifiant[identifiant.SK_ID_CURR==chosen_customer]])[0] * 100000
    
    st.sidebar.write(pred)
    
else:
    st.write("Vous entrerez une à une les informations du client!")
 
    
