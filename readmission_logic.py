# Conditions whose patients were readmitted in >= 98% of cases in hospital_data_analysis.csv
HIGH_RISK_CONDITIONS = {"Heart Attack", "Heart Disease"}


def predict_readmission(condition, length_of_stay):
    if condition in HIGH_RISK_CONDITIONS and length_of_stay >= 1:
        return "READMIT"
    else:
        return "NO READMIT"


if __name__ == "__main__":
    result = predict_readmission("Heart Attack", 7)
    print("Predicted Readmission:", result)
