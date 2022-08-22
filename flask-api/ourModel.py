from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


def price_and_demand_predict(Item, State, Weekend, Grade, Organic, RPS, DFD, Freshness, Seasonal, Otipy_certified, Unique_Customors):
    dataset = pd.read_csv("./AgriTech_Dataset.csv")
    X = dataset.iloc[:, 1:-2].values
    y = dataset.iloc[:, [-1, -2]].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X_train)
    regressor = LinearRegression()
    regressor.fit(X_poly, y_train)
    X_test = [[Item, State, Weekend, Grade, Organic, RPS, DFD,
               Freshness, Seasonal, Otipy_certified, Unique_Customors]]
    y_pred = regressor.predict(poly_reg.transform(X_test))
    prediction = {
        "Item": Item,
        "State": State,
        "Weekend": Weekend,
        "Grade": Grade,
        "Organic": Organic,
        "RPS": RPS,
        "DFD": DFD,
        "Freshness": Freshness,
        "Seasonal": Seasonal,
        "Otipy_Certified": Otipy_certified,
        "Unique_Customers": Unique_Customors,
        "Price_Predicted": round(y_pred[0, 1], 2),
        "Demand_Predicted": round(y_pred[0, 0], 2)
    }
    return prediction


def demand_predict(Item, State, Weekend, Grade, Organic, RPS, DFD, Freshness, Seasonal, Otipy_certified, Unique_Customors, Price):
    dataset = pd.read_csv("./AgriTech_Dataset.csv")
    X = dataset.iloc[:, 1:-1].values
    y = dataset.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X_train)
    regressor = LinearRegression()
    regressor.fit(X_poly, y_train)
    X_test = [[Item, State, Weekend, Grade, Organic, RPS, DFD,
               Freshness, Seasonal, Otipy_certified, Unique_Customors, Price]]
    y_pred = regressor.predict(poly_reg.transform(X_test))
    prediction = {
        "Item": Item,
        "State": State,
        "Weekend": Weekend,
        "Grade": Grade,
        "Organic": Organic,
        "RPS": RPS,
        "DFD": DFD,
        "Freshness": Freshness,
        "Seasonal": Seasonal,
        "Otipy_Certified": Otipy_certified,
        "Unique_Customers": Unique_Customors,
        "Price": Price,
        "Demand_Predicted": round(y_pred[0], 2)
    }
    return prediction


def price_predict(Item, State, Weekend, Grade, Organic, RPS, DFD, Freshness, Seasonal, Otipy_certified, Unique_Customors, Demand):
    dataset = pd.read_csv("./AgriTech_Dataset.csv")
    X = dataset.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]].values
    y = dataset.iloc[:, -2].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    regressor = RandomForestRegressor(n_estimators=20, random_state=0)
    regressor.fit(X_train, y_train)
    X_test = [[Item, State, Weekend, Grade, Organic, RPS, DFD,
               Freshness, Seasonal, Otipy_certified, Unique_Customors, Demand]]
    y_pred = regressor.predict(X_test)
    prediction = {
        "Item": Item,
        "State": State,
        "Weekend": Weekend,
        "Grade": Grade,
        "Organic": Organic,
        "RPS": RPS,
        "DFD": DFD,
        "Freshness": Freshness,
        "Seasonal": Seasonal,
        "Otipy_Certified": Otipy_certified,
        "Unique_Customers": Unique_Customors,
        "Demand": Demand,
        "Price_Predicted": round(y_pred[0], 2)
    }
    return prediction
