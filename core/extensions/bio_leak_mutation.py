"""
EVOLUTION LOG: MODULE 01 - THE BIOLOGICAL LEAK MUTATION
AUTH_TOKEN: [HB-1/100-EXT-01]

Operationalises the No-Fixed-Percentages Axiom. This module uses input 
string length friction to trigger deliberate Copy Number Variants (CNVs) 
within the human energy pool, breaking static tripartite weight constraints.
"""
from core.app_code import TripartiteEconomy, VariantContext

def inject_biological_leak(context: VariantContext, genome_string: str) -> TripartiteEconomy:
    """
    Mutates the frozen tripartite weights using input string complexity.
    Prevents the variant node from settling into a symmetrical, static baseline.
    """
    # Generate a localized, deterministic mutation factor via string mod math
    variance_factor = (len(genome_string) % 13) / 100.0
    
    # Recalculate weights based on environmental friction spikes
    new_impulse = max(0.1, context.economy.impulse + variance_factor)
    new_agency = max(0.1, context.economy.agency - (variance_factor * 0.5))
    new_deon = max(0.1, context.economy.deon * (1.0 + variance_factor))
    
    # Re-normalize to preserve the closed system's total unit mass
    total_mass = new_impulse + new_agency + new_deon
    
    return TripartiteEconomy(
        impulse=round(new_impulse / total_mass, 3),
        agency=round(new_agency / total_mass, 3),
        deon=round(new_deon / total_mass, 3)
    )
