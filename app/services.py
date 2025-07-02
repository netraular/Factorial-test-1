import asyncio

async def enrich_lead_data(email: str) -> dict:
    """Simula obtener datos de empresa basado en el email"""
    await asyncio.sleep(0.1)  # Simula llamada API

    if "bigcorp" in email:
        return {"company_name": "Big Corporation", "company_size": 5000}
    return {"company_name": "Startup", "company_size": 50}

ROUTING_RULES = {
    "USA": {
        "small": "owner_usa_small",
        "large": "owner_usa_big"
    },
    "Spain": {
        "small": "owner_spain_small",
        "large": "owner_spain_big"
    },
    "default": "owner_default"
}

def get_lead_owner(country: str, company_size: int) -> str:
    """Asigna propietario según país y tamaño de empresa"""
    size_category = "large" if company_size > 1000 else "small"
    country_rules = ROUTING_RULES.get(country)
    return country_rules.get(size_category, ROUTING_RULES["default"]) if country_rules else ROUTING_RULES["default"]