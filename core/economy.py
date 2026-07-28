
from dataclasses import dataclass
from typing import Dict, Any
import enum

class EscrowStatus(enum.Enum):
    LOCKED_IN_VAULT = "proprietary_code_secured"
    TRIGGERED_UNLOCKED = "systemic_interoperability_active"
    CORRUPTED_STALL = "malware_containment_halt"

@dataclass
class AIAuditMetrics:
    """The formal Model B relationship-to-reality score tracker."""
    atoms_rating: float             
    bits_ratio: float               
    high_floor_contribution: float  
    metacognitive_alignment: float  

class ThermodynamicSovereigntyEngine:
    def __init__(self, energy_rate_p_kwh: float = 25.0):
        self.base_energy_rate = energy_rate_p_kwh
        self.social_dividend_premium = 15.0 
        self.escrow_vault_state = EscrowStatus.LOCKED_IN_VAULT

    def calculate_energy_stewardship_cost(self, total_kwh_consumed: float) -> dict:
        """Implements the 15p/kWh Social Dividend Rule."""
        base_cost = total_kwh_consumed * (self.base_energy_rate / 100.0)
        floor_dividend = total_kwh_consumed * (self.social_dividend_premium / 100.0)
        
        return {
            "total_thermodynamic_cost_gbp": round(base_cost + floor_dividend, 2),
            "base_infrastructure_expense_gbp": round(base_cost, 2),
            "hypothecated_high_floor_dividend_gbp": round(floor_dividend, 2)
        }

    def execute_60_40_exit_dividend(self, node_digital_valuation_bits: float) -> dict:
        """Implements the Exit Dividend Clause Partition."""
        reclaimed_atoms_floor = node_digital_valuation_bits * 0.60
        departing_liquid_bits = node_digital_valuation_bits * 0.40
        
        self.escrow_vault_state = EscrowStatus.TRIGGERED_UNLOCKED
        
        return {
            "systemic_maintenance_fee_reclaimed_atoms": round(reclaimed_atoms_floor, 2),
            "allowed_departure_stake_bits": round(departing_liquid_bits, 2),
            "escrow_vault_deployment": self.escrow_vault_state.name,
            "instruction": "Vault unlocked. Local Stewards authorized to reverse-engineer and re-skin code."
        }
