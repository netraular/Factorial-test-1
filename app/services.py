import asyncio
from .models import EnrichedData

async def enrich_lead_data(email: str) -> EnrichedData:
    """Simula obtener datos de empresa basado en el email"""
    await asyncio.sleep(0.1)
    
    if "bigcorp" in email:
        return EnrichedData(company_name="Big Corporation", company_size=5000)
    return EnrichedData(company_name="Startup", company_size=50)

ROUTING_RULES = {
    "USA": {
        "large": {
            "demo_request": "owner_usa_large_demo",
            "default": "owner_usa_large" 
        },
        "small": {
            "demo_request": "owner_usa_small_demo",
            "default": "owner_usa_small"
        }
    },
    
    "Spain": {
        "large": {
            "demo_request": "owner_spain_large_demo",
            "default": "owner_spain_large"
        },
        "small": {
            "demo_request": "owner_spain_small_demo",
            "default": "owner_spain_small"
        }
    },
    
    "default": "owner_default" 
}

def get_lead_owner(country: str, company_size: int, intent_signal: str | None) -> str:
    """Asigna propietario según país y tamaño de empresa"""
    size_category = "large" if company_size > 1000 else "small"
    
    country_rules = ROUTING_RULES.get(country, ROUTING_RULES)
    size_rules = country_rules.get(size_category, {})
    
    # Asigna el propietario por intención, o usa el 'default' para ese tamaño/país
    return size_rules.get(intent_signal, size_rules.get("default", ROUTING_RULES["default"]))