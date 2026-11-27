#  Used Car Price Prediction

A Machine Learning web application that predicts the resale price of a used car based on its specifications, including brand, manufacturing year, mileage, kilometers driven, fuel type, transmission, engine capacity and more.

##  Live Demo

**Try the application here:** [Used Car Price Predictor](https://car-price-prediction-5zrmj8nlsfcbnvlg9bsryf.streamlit.app/)

##  Project Overview

Buying or selling a used car can be challenging because its resale value depends on several factors. This project uses Machine Learning to estimate the resale price of a used car based on its features.

The model was trained on used car data and deployed through an interactive Streamlit application, allowing users to enter car details and receive an estimated price.

##  Features

- Predicts the estimated resale price of a used car.
- Interactive and user-friendly interface.
- Takes multiple car attributes as input.
- Machine Learning pipeline with preprocessing and prediction.
- Handles categorical and numerical features.
- Deployed as a web application using Streamlit.

##  Input Features

| Feature | Description |
|---|---|
| Car Name | Car brand/name |
| Location | City where the car is listed |
| Year | Manufacturing year |
| Kilometers Driven | Total distance driven |
| Fuel Type | Petrol, Diesel, CNG, etc. |
| Transmission | Manual or Automatic |
| Owner Type | First, Second, Third, etc. |
| Mileage | Mileage in km/l |
| Engine | Engine capacity in CC |
| Power | Engine power in bhp |
| Seats | Number of seats |

##  Machine Learning

The project uses a Machine Learning regression model to estimate the resale price of a car.

### Model Pipeline

- Data preprocessing
- Handling missing values
- Feature engineering
- Encoding categorical features
- Model training and evaluation
- Final model training
- Model deployment

### Evaluation Metrics

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Git & GitHub

##  How to Use

1. Open the deployed application.
2. Enter the car's details.
3. Select the relevant car specifications.
4. Click the prediction button.
5. View the estimated resale price.

##  Project Structure

```text
car-price-prediction/
│
├── app.py
├── car_price_model.pkl
├── requirements.txt
└── README.md
```

##  Model Performance

- **MAE:** 1.4776 Lakhs
- **RMSE:** 3.5935 Lakhs
- **R² Score:** 0.8951

*These metrics are based on the model's validation evaluation.*

## 👨‍💻 Author

Developed as a Machine Learning project to explore regression, data preprocessing, model evaluation and web application deployment.
