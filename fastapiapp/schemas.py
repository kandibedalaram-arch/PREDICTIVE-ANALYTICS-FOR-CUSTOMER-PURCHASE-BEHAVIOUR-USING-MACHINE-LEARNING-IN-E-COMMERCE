from pydantic import BaseModel

class PurchaseInput(BaseModel):
    Age: int
    Gender: int
    AnnualIncome: float
    NumberOfPurchases: int
    ProductCategory: int
    TimeSpentOnWebsite: float
    LoyaltyProgram: int
    DiscountsAvailed: int
