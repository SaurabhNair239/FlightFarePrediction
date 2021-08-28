
import pickle
import pandas as pd
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    return render_template('/index.html')
@app.route('/predict',methods=['POST'])
def val_cal():
    try:
        if request.method == 'POST':
            temp_list = []
            dep_date = request.form['Dep_Date_Time']
            arr_date = request.form['Arr_Date_Time']
            source = request.form['A_airport']
            destination = request.form['D_airport']
            airlines = request.form['Airlines']
            n_stops = int(request.form['n_stops'])

            #Departure

            d_date = int(pd.to_datetime(dep_date).day)
            d_month = int(pd.to_datetime(dep_date).month)
            d_hour = int(pd.to_datetime(dep_date).hour)
            d_min = int(pd.to_datetime(dep_date).minute)

            #Arrival

            a_hour = int(pd.to_datetime(arr_date).hour)
            a_min = int(pd.to_datetime(arr_date).minute)

            dur_hour = a_hour-d_hour
            dur_min = a_min-d_min

           #Source
            if source == 'Bangalore':
                Source_Bangalore = 1
                Source_Chennai = 0
                Source_Delhi = 0
                Source_Kolkata = 0
                Source_Mumbai = 0
            elif source == 'Chennai':
                Source_Bangalore = 0
                Source_Chennai = 1
                Source_Delhi = 0
                Source_Kolkata = 0
                Source_Mumbai = 0
            elif source == 'Delhi':
                Source_Bangalore = 0
                Source_Chennai = 0
                Source_Delhi = 1
                Source_Kolkata = 0
                Source_Mumbai = 0
            elif source == 'Kolkata':
                Source_Bangalore = 0
                Source_Chennai = 0
                Source_Delhi = 0
                Source_Kolkata = 1
                Source_Mumbai = 0
            elif source == 'Mumbai':
                Source_Bangalore = 0
                Source_Chennai = 0
                Source_Delhi = 0
                Source_Kolkata = 0
                Source_Mumbai = 1

            #Destination
            if destination == 'Bangalore':
                Destination_Bangalore = 1
                Destination_Kochin = 0
                Destination_Delhi = 0
                Destination_Hyderabad = 0
                Destination_Kolkata = 0
                Destination_New_Delhi = 0
            elif source == 'Kochin':
                Destination_Bangalore = 0
                Destination_Kochin = 1
                Destination_Delhi = 0
                Destination_Hyderabad = 0
                Destination_Kolkata = 0
                Destination_New_Delhi = 0
            elif source == 'Delhi':
                Destination_Bangalore = 0
                Destination_Kochin = 0
                Destination_Delhi = 1
                Destination_Hyderabad = 0
                Destination_Kolkata = 0
                Destination_New_Delhi = 0
            elif source == 'Hyderabad':
                Destination_Bangalore = 0
                Destination_Kochin = 0
                Destination_Delhi = 0
                Destination_Hyderabad = 1
                Destination_Kolkata = 0
                Destination_New_Delhi = 0
            elif source == 'Kolkata':
                Destination_Bangalore = 0
                Destination_Kochin = 0
                Destination_Delhi = 0
                Destination_Hyderabad = 0
                Destination_Kolkata = 1
                Destination_New_Delhi = 0
            elif source == 'New Delhi':
                Destination_Bangalore = 0
                Destination_Kochin = 0
                Destination_Delhi = 0
                Destination_Hyderabad = 0
                Destination_Kolkata = 0
                Destination_New_Delhi = 1

            #Airlines
            if airlines == 'Air Asia':
                Airlines_Air_Asia = 1
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0
            elif airlines == 'Air India':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 1
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0
            elif airlines == 'GoAir':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 1
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0
            elif airlines == 'Indigo':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 1
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0
            elif airlines == 'Jet Airways':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 1
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0
            elif airlines == 'Multiple carriers':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 1
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0
            elif airlines == 'Multiple carriers Premium economy':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 1
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0
            elif airlines == 'SpiceJet':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 1
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0

            elif airlines == 'Trujet':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 1
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0

            elif airlines == 'Vistara':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 1
                Airline_Vistara_Premium_economy = 0

            elif airlines == 'Vistara Premium economy':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 0
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 1

            elif airlines == 'Jet Airways Business':
                Airlines_Air_Asia = 0
                Airlines_Air_India = 0
                Airlines_GoAir = 0
                Airline_IndiGo = 0
                Airline_Jet_Airways = 0
                Airline_Jet_Airways_Business = 1
                Airline_Multiple_carriers = 0
                Airline_Multiple_carriers_Premium_economy = 0
                Airline_SpiceJet = 0
                Airline_Trujet = 0
                Airline_Vistara = 0
                Airline_Vistara_Premium_economy = 0

            #sending to model
            filename = 'xgboost_model.pickle'
            model = pickle.load(open(filename, 'rb'))
            test_set = pd.DataFrame([[n_stops,dur_hour,dur_min,d_date,d_month,d_min,d_hour,a_min,a_hour,Airlines_Air_Asia,Airlines_Air_India,Airlines_GoAir,Airline_IndiGo,Airline_Jet_Airways,Airline_Jet_Airways_Business,Airline_Multiple_carriers,Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,Source_Bangalore,Source_Chennai,Source_Delhi,Source_Kolkata,Source_Mumbai,Destination_Bangalore,Destination_Kochin,Destination_Delhi,Destination_Hyderabad,Destination_Kolkata,Destination_New_Delhi]])
            cols_when_model_builds = model.get_booster().feature_names
            test_set.columns = cols_when_model_builds
            prediction = model.predict(test_set)
            prediction = prediction.round(2)
            return render_template('/predict.html',ans = prediction)
    except:
        print('Error in main.py File')

if __name__ == '__main__':
    app.run(debug=True)
