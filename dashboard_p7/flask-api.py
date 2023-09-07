from flask import Flask,  redirect, url_for ,request, jsonify
import urllib3
import pandas as pd
import numpy as np
import joblib
import json

app = Flask(__name__)

classify_mappings = {0: 'Bon client', 1: 'Client à risque'}
path_server = 'http://127.0.0.1:5000/'

@app.route('/load-agg-data')
def get_agg_data():
    # amelioration création base de données
    try:                
        # pour recuperer les resultats use open url
        important_features = joblib.load('support/data/list_col_to_keep.joblib')
        data1 = pd.read_csv("support/data/application_train.csv", usecols=important_features+['TARGET','SK_ID_CURR'] )
        data2 = pd.read_csv("support/data/application_test.csv",  usecols= important_features+['SK_ID_CURR'] )
    
        # Données numériques
        number_data = data1.select_dtypes(include = np.number).groupby(['TARGET']).agg(pd.Series.median).T
    
        # Données catégorielles
        categ_data_data = data1.groupby(['TARGET']).agg(pd.Series.mode).select_dtypes(exclude = np.number).T
    
        data_agg = pd.concat([number_data, categ_data_data],axis=0)
        data_agg.reset_index(inplace=True)
        data_agg.rename(columns={'index':'info', 0:'Bon', 1:'Mauvais'},inplace = True)
        
        data = pd.concat([data1, data2],axis=0).drop_duplicates()
        # data = pd.concat([data1.drop(columns = ['TARGET']), data2],axis=0).drop_duplicates()
        # Some simple new features (percentages)
        data['INCOME_CREDIT_PERC'] = data['AMT_INCOME_TOTAL'] / data['AMT_CREDIT']
        data['time_to_repay'] = data['AMT_CREDIT'] / data['AMT_ANNUITY']
        data['ANNUITY_INCOME_PERC'] = data['AMT_ANNUITY'] / data['AMT_INCOME_TOTAL']
        data = data[data['CODE_GENDER'] != 'XNA']
        for bin_feature in ['CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY']:
            data[bin_feature], uniques = pd.factorize(data[bin_feature])
        return jsonify( {'data':data.to_dict('records'), 'data_agg':data_agg.to_dict('records')} ) 
    except:
        return 'Aggregation data NOT available!'
    

@app.route('/load_data')
def get_data():
    # amelioration création base de données
    try:
        df_train = pd.read_csv('support/data/application_train.csv' )
        df_test = pd.read_csv('support/data/application_test.csv' )
        list_index = list(set(df_train.SK_ID_CURR.to_list() + df_test.SK_ID_CURR.to_list())) # a tester
        columns_to_keep = joblib.load("support/data/list_col_to_keep.joblib")

        # concatened dataframe
        data = pd.concat([df_train,df_test], axis = 0)

        # Filtered columns
        data = data[['SK_ID_CURR','TARGET']+columns_to_keep]

        #feature ingenering
        data = data[data['CODE_GENDER'] != 'XNA']
        data['INCOME_CREDIT_PERC'] = data['AMT_INCOME_TOTAL'] / data['AMT_CREDIT']
        data['time_to_repay'] = data['AMT_CREDIT'] / data['AMT_ANNUITY']
        data['ANNUITY_INCOME_PERC'] = data['AMT_ANNUITY'] / data['AMT_INCOME_TOTAL']
        for bin_feature in ['CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY']:
            data[bin_feature], uniques = pd.factorize(data[bin_feature])
                
        # pour recuperer les resultats use open url
        return jsonify({'index':list_index, 'data':data.to_dict('records')})
    except:
        return 'Data NOT available!'
    # http://127.0.0.1:5000/load_data
    

@app.route('/predict/index',methods=['GET'])
def index_predict():
    # get index
    idClient = int(request.args.get('idClient'))
    # get data
    try:
        http = urllib3.PoolManager()
        r = http.request('GET',path_server+'load_data')
        resData = json.loads(r.data)
    except:
        return 'loading api not available'

    if idClient in resData['index']:
        # filtered data
        valideData = pd.DataFrame.from_dict(resData['data'])
        valideData = valideData.loc[valideData.SK_ID_CURR == idClient,:].drop(columns = ['SK_ID_CURR','TARGET'])
        return redirect(url_for('values_predict',values = valideData.to_json(orient="columns") ))
    else:
        return 'Id non reconnu'
    # http://127.0.0.1:5000/predict/index?idClient=274986


@app.route('/predict/values',methods=['GET'])
def values_predict():
    # get data
    dict_data = request.args.get('values')
    # restructuration de la données
    dict_data = pd.DataFrame(json.loads(dict_data) )
    # probability
    probability = model.predict_proba(dict_data)[0][1]
    #decision
    decision = model.predict( dict_data) 
    decision = int( decision )
    return jsonify({'proba':probability, 'decision': classify_mappings[decision]  })
    # http://127.0.0.1:5000/predict/values?values=%7B%22AMT_ANNUITY%22%3A%7B%220%22%3A16713.0%7D,%22AMT_CREDIT%22%3A%7B%220%22%3A288873.0%7D,%22AMT_INCOME_TOTAL%22%3A%7B%220%22%3A67500.0%7D,%22ANNUITY_INCOME_PERC%22%3A%7B%220%22%3A0.2476%7D,%22CNT_CHILDREN%22%3A%7B%220%22%3A0%7D,%22CODE_GENDER%22%3A%7B%220%22%3A0%7D,%22DAYS_BIRTH%22%3A%7B%220%22%3A-16963%7D,%22DAYS_EMPLOYED%22%3A%7B%220%22%3A-1746%7D,%22EXT_SOURCE_2%22%3A%7B%220%22%3A0.657665461%7D,%22EXT_SOURCE_3%22%3A%7B%220%22%3A0.7091891097%7D,%22FLAG_OWN_CAR%22%3A%7B%220%22%3A0%7D,%22FLAG_OWN_REALTY%22%3A%7B%220%22%3A0%7D,%22INCOME_CREDIT_PERC%22%3A%7B%220%22%3A0.2336666978%7D,%22NAME_EDUCATION_TYPE%22%3A%7B%220%22%3A%22Secondary+%5C%2F+secondary+special%22%7D,%22NAME_FAMILY_STATUS%22%3A%7B%220%22%3A%22Married%22%7D,%22NAME_INCOME_TYPE%22%3A%7B%220%22%3A%22Working%22%7D,%22OCCUPATION_TYPE%22%3A%7B%220%22%3A%22Laborers%22%7D,%22ORGANIZATION_TYPE%22%3A%7B%220%22%3A%22Business+Entity+Type+3%22%7D,%22REG_CITY_NOT_LIVE_CITY%22%3A%7B%220%22%3A0%7D,%22REG_CITY_NOT_WORK_CITY%22%3A%7B%220%22%3A0%7D,%22REG_REGION_NOT_LIVE_REGION%22%3A%7B%220%22%3A0%7D,%22REG_REGION_NOT_WORK_REGION%22%3A%7B%220%22%3A0%7D,%22time_to_repay%22%3A%7B%220%22%3A17.2843295638%7D%7D


if __name__ == '__main__':
    model = joblib.load("support\models\HistGradientBoostingClassifier_model.sav") # Load "model.pkl"
    print ('Model loaded')
    
    app.run(debug=True, use_reloader = True)