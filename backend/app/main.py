from fastapi import FastAPI
from logic import liquidity_crunch, interest_rate_shock, credit_crisis
from logic import simulate_valuation

app = FastAPI(title="Crisis Risk Simulator")

@app.get("/")
def root():
    return {"status": "Crisis Risk Simulator running"}

@app.get("/simulate")
def simulate(entity: str, crisis: str):
    crisis = crisis.lower().strip()

    if crisis == "liquidity":
        return liquidity_crunch(entity)
    elif crisis == "rates":
        return interest_rate_shock(entity)
    elif crisis == "credit":
        return credit_crisis(entity)

    return {
        "error": "Invalid crisis type. Use: liquidity | rates | credit"
    }

@app.get("/simulate_valuation")
def simulate_valuation_api(entity: str, crisis: str, base_earnings: float, multiple: float):
    crisis = crisis.lower().strip()
    return simulate_valuation(
        base_earnings=base_earnings,
        multiple=multiple,
        crisis=crisis,
        entity=entity
    )
