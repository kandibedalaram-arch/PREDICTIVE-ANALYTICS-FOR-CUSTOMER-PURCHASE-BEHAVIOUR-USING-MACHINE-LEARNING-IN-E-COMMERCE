from fastapi import FastAPI
from fastapiapp.schemas import PurchaseInput
from fastapiapp.model import model

fastapiapp = FastAPI()


@fastapiapp.get("/")
def home():
    return {"message": "Purchase Prediction API is running"}


@fastapiapp.post("/predict")
def predict(data: PurchaseInput):

    # Feature Engineering

    # IncomeLevel
    # Need thresholds from training dataset
    # Temporary placeholder
    if data.AnnualIncome < 50000:
        income_level = 0
    elif data.AnnualIncome < 80000:
        income_level = 1
    else:
        income_level = 2

    customer_activity_index = (
        data.NumberOfPurchases * data.TimeSpentOnWebsite
    )

    recency_frequency = (
        data.NumberOfPurchases /
        (data.TimeSpentOnWebsite + 1)
    )

    engagement_score = (
        0.5 * data.TimeSpentOnWebsite +
        0.3 * data.NumberOfPurchases +
        0.2 * data.DiscountsAvailed
    )

    input_data = [[
        data.Age,
        data.Gender,
        data.AnnualIncome,
        data.NumberOfPurchases,
        data.ProductCategory,
        data.TimeSpentOnWebsite,
        data.LoyaltyProgram,
        data.DiscountsAvailed,
        engagement_score,
        recency_frequency,
        customer_activity_index,
        income_level
    ]]
    result=model.predict(input_data)[0]
    label = "Will Purchase" if result == 1 else "Will Not Purchase"
    return {
    "prediction": int(result),
    "result": label
    }

    
