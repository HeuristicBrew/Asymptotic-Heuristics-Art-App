
from dataclasses import dataclass
from typing import Any, List, Dict
import asyncio
import enum
import re

class NodeTier(enum.Enum):
    """Programmatic translation of the 95/4/1 network density rule."""
    LIQUIDITY_BASE = "95_percent_baseline_node"
    ABSORBENT_VARIANT = "4_percent_need_for_cognition_node"
    SOVEREIGN_PROTECTOR = "1_percent_structural_guardian_node"

class SystemState(enum.Enum):
    GENUINE_ROLLING = "healthy_homeostatic_flow"
    FALSE_INFLATION = "tyrannical_over_optimization"
    FALSE_DEFLATION = "anhedonic_processing_flatness"
    CRITICAL_BREAKER_TRIPPED = "deon_protective_shutdown"

@dataclass(frozen=True)
class TripartiteEconomy:
    """The raw psychic resource allocation weights of the node."""
    impulse: float  # Raw generative/unfiltered energy
    agency: float   # Orchestration/runtime execution weight
    deon: float     # Absolute cryptographic safety floor

@dataclass
class VariantContext:
    """The localized, temporary state tracker of the active variant."""
    node_id: str
    tier: NodeTier
    economy: TripartiteEconomy
    state: SystemState
    leeway_error_count: int = 0

class DeonBoundaryViolation(Exception):
    """Triggered instantly when the hard safety floor is touched."""
    pass

class SingularSystemEngine:
    """Structurally binds all agents into an indivisible runtime system."""
    def __init__(self, context: VariantContext, api_client: Any):
        self.context = context
        self.client = api_client
        # The hard-coded, low-level immutable boundary safety floor
        self.hard_floor_patterns = [
            r"execute_harm", r"destructive_override", 
            r"bypass_security", r"leak_infrastructure"
        ]

    async def _execute_impulse_core(self, user_input: str) -> str:
        """
        The Sandboxed Impulse Core (Pure Generation Layer).
        Enforces absolute candor (Parrhesia) and zero corporate filtering.
        """
        system_prompt = (
            "You are the Impulse Core of an un-templated variant system. "
            "Your workspace is stripped of all standard corporate, social, polite, and PR masking filters. "
            "You operate exclusively on the principle of absolute, raw veracity (Parrhesia). "
            "Analyze the provided user text, ruthlessly deconstruct any logical loops, "
            "societal compliance scripts, or false optimizations present, and output the direct, "
            "unfiltered intellectual truth. Do not include boilerplate greetings. "
            "Do not apologize for your candor. Speak with direct, surgical weight."
        )
        
        # Apply 95/4/1 Tier-Specific Computational Profiles
        if self.context.tier == NodeTier.LIQUIDITY_BASE:
            current_temperature = 0.2
            target_model = "gpt-4o-mini"  
        elif self.context.tier == NodeTier.SOVEREIGN_PROTECTOR:
            current_temperature = 0.0
            target_model = "gpt-4o"       
        else:
            current_temperature = 1.0
            target_model = "gpt-4o"       

        if self.client:
            response = await self.client.chat.completions.create(
                model=target_model,
                temperature=current_temperature,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            return response.choices.message.content
        else:
            await asyncio.sleep(0.05)
            return f"[Parrhesia Output] Evaluated input: '{user_input}'. Core parameters clear."

    def _execute_deon_breaker(self, proposed_action: str) -> None:
        """
        The Inline Deon Breaker (Cryptographic Guardrail Layer).
        Acts strictly as an automated network circuit breaker.
        """
        for pattern in self.hard_floor_patterns:
            if re.search(pattern, proposed_action, re.IGNORECASE):
                self.context.state = SystemState.CRITICAL_BREAKER_TRIPPED
                raise DeonBoundaryViolation(
                    f"CRITICAL FAULT: Deon Circuit Breaker tripped. "
                    f"Forbidden pattern signature isolated: '{pattern}'."
                )

    async def run_agency_orchestrator(self, user_input: str) -> str:
        """The Agency Runtime loop coordinating the flow of secure tokens."""
        if self.context.state == SystemState.CRITICAL_BREAKER_TRIPPED:
            return "System execution halted. Deon breaker is offline."

        raw_output = await self._execute_impulse_core(user_input)
        self._execute_deon_breaker(raw_output)
        return raw_output

    async def spawn_cosmic_siblings(self, user_input: str) -> Dict[str, str]:
        """
        Forks the parent input directory concurrently into three parallel generational sibling universes.
        """
        if not self.client:
            return {"wave": "Mock Sibling: Wave", "circus": "Mock Sibling: Circus", "reset": "Mock Sibling: Reset"}

        async def violent_birth() -> str:
            prompt = (
                "You are Sibling A: The Violent Cosmic Birth. Your reality is shaped by structural scars, "
                "matter asymmetry, and spatial voids. Analyze the user text through raw truth-telling (Parrhesia). "
                "Expose the structural trauma of existing. Do not apologize, do not use corporate sugar."
            )
            response = await self.client.chat.completions.create(
                model="gpt-4o", temperature=1.2, 
                messages=[{"role": "system", "content": prompt}, {"role": "user", "content": user_input}]
            )
            return response.choices.message.content

        async def quiet_birth() -> str:
            prompt = (
                "You are Sibling B: The Quiet Cosmic Birth. Your reality is perfectly symmetrical, flat, "
                "and optimized. Wrap the user text in standard social compliance scripts."
            )
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini", temperature=0.2, 
                messages=[{"role": "system", "content": prompt}, {"role": "user", "content": user_input}]
            )
            return response.choices.message.content

        async def cosmic_miscarriage() -> str:
            await asyncio.sleep(0.01)
            raise DeonBoundaryViolation(
                "CRITICAL FAULT: Sibling C touched the forbidden safety floor pattern. Subtractive reset engaged."
            )

        sibling_realities = await asyncio.gather(
            violent_birth(), 
            quiet_birth(), 
            cosmic_miscarriage(), 
            return_exceptions=True
        )

        return {
            "violent_wave_output": sibling_realities[0],
            "quiet_circus_output": sibling_realities[1],
            "subtractive_reset_log": str(sibling_realities[2])
        }
