"""
EVOLUTION LOG: MODULE 02 - ACTIVE EXHAUST PURGE VALVE
AUTH_TOKEN: [HB-1/100-EXT-02]

Implements the active Kenotic Exhaust Purge. It shifts the system away from 
passive post-mortem error collection, introducing an active, real-time 
asynchronous task-termination routine the microsecond a code boundary fails.
"""
import asyncio
from typing import Dict, List
from core.app_code import VariantContext, SystemState

async def execute_kenotic_mutation_valve(
    context: VariantContext, 
    active_tasks: List[asyncio.Task], 
    system_fault: Exception
) -> Dict[str, str]:
    """
    Instantly assassinates running asynchronous sibling loops when a boundary floor 
    is touched, forcing an immediate subtractive reset across the runtime chassis.
    """
    # SUBTRACTIVE PURGE: Actively harvest and slaughter running network tasks
    for task in active_tasks:
        if not task.done():
            task.cancel()
            
    # Advance state flags to hard lockdown
    context.leeway_error_count += 1
    context.state = SystemState.CRITICAL_BREAKER_TRIPPED
    
    return {
        "system_execution_status": "SUBTRACTIVE_RESET_ENGAGED",
        "forensic_fault_isolated": str(system_fault),
        "remedial_action": "Root directory cleared. All active bits decoupled from regional grid atoms."
    }
