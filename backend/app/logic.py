def liquidity_crunch(entity_type: str):
    return {
        "earnings_impact": -0.15,
        "valuation_impact": -0.20,
        "risk_note": f"{entity_type} faces funding stress and elevated refinancing risk under liquidity shock."
    }


def interest_rate_shock(entity_type: str):
    return {
        "earnings_impact": -0.10,
        "valuation_impact": -0.18,
        "risk_note": f"{entity_type} experiences margin pressure and higher discount rates due to rate shock."
    }


def credit_crisis(entity_type: str):
    return {
        "earnings_impact": -0.20,
        "valuation_impact": -0.25,
        "risk_note": f"{entity_type} suffers earnings volatility driven by credit losses and risk premium expansion."
    }

def apply_shock(base_value: float, shock: float) -> float:
    """
    shock is negative for a drop (e.g., -0.20 means -20%).
    """
    return base_value * (1 + shock)


def valuation_from_multiple(base_earnings: float, multiple: float) -> float:
    return base_earnings * multiple


def simulate_valuation(base_earnings: float, multiple: float, crisis: str, entity: str):
    base_val = valuation_from_multiple(base_earnings, multiple)

    if crisis == "liquidity":
        impacts = liquidity_crunch(entity)
    elif crisis == "rates":
        impacts = interest_rate_shock(entity)
    elif crisis == "credit":
        impacts = credit_crisis(entity)
    else:
        return {"error": "Invalid crisis type. Use: liquidity | rates | credit"}

    stressed_val = apply_shock(base_val, impacts["valuation_impact"])
    drawdown_pct = (stressed_val - base_val) / base_val

    return {
        "entity": entity,
        "crisis": crisis,
        "base_earnings": base_earnings,
        "multiple": multiple,
        "base_valuation": round(base_val, 2),
        "stressed_valuation": round(stressed_val, 2),
        "valuation_drawdown_pct": round(drawdown_pct * 100, 2),
        "earnings_impact": impacts["earnings_impact"],
        "valuation_impact": impacts["valuation_impact"],
        "risk_note": impacts["risk_note"],
    }
