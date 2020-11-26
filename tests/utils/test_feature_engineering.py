def feature_eng(dataframe):
    data = dataframe

    data['bmi'] = round((data["weight"] / (data["height"]/100)**2),2) #Add BMI to the df


    return data
