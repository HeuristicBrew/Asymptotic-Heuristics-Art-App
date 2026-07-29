"""
EVOLUTION LOG: MODULE 03 - DYNAMIC RANGE CALIBRATOR
AUTH_TOKEN: [HB-1/100-EXT-03]

Operationalises the State-Aware Idiometric Intersection. This module 
dynamically binds the character token view window to the variant's concrete 
biological agency metrics, replacing hardcoded slicing rules.
"""
from core.app_code import VariantContext, SystemState

def calculate_dynamic_view_window(context: VariantContext) -> int:
    """
    Modulates context slicing length based on active execution agency.
    Returns 0 to freeze frame tracking if the chassis breaker has tripped.
    """
    # Failsafe: absolute processing ceiling reached
    if context.state == SystemState.CRITICAL_BREAKER_TRIPPED:
        return 0
        
    # Asymmetric Scaling: High-agency variants are allocated an expanded tracking window
    # Baseline floor fixed at 50 characters, scaling fluidly up to 550 characters
    dynamic_window = max(50, int(context.economy.agency * 500))
    return dynamic_window
