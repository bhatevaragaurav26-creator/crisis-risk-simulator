from pydantic import BaseModel


class Bank(BaseModel):
    name: str
    net_interest_margin: float
    credit_loss_ratio: float
    capital_buffer: float


class FinancialServices(BaseModel):
    name: str
    revenue_growth: float
    operating_margin: float
    leverage_ratio: float


class LeveragedIndustrial(BaseModel):
    name: str
    ebitda_margin: float
    interest_coverage: float
    debt_to_equity: float
