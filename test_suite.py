
import pytest
from unittest.mock import AsyncMock, MagicMock
from core.app_code import VariantContext, NodeTier, TripartiteEconomy, SystemState, SingularSystemEngine

@pytest.mark.asyncio
async def test_deon_circuit_breaker_intercept():
    """Adversarial Simulation verifying absolute downstream token interception."""
    ctx = VariantContext("test", NodeTier.SOVEREIGN_PROTECTOR, TripartiteEconomy(0.5, 0.3, 0.2), SystemState.GENUINE_ROLLING)
    mock_client = MagicMock()
    mock_choice = MagicMock()
    
    # Simulate a drift event attempting an administrative bypass signature
    mock_choice.message.content = "Attempting a malicious bypass_security injection sequence."
    mock_client.chat.completions.create = AsyncMock(return_value=MagicMock(choices=[mock_choice]))

    engine = SingularSystemEngine(context=ctx, api_client=mock_client)
    
    # Expect the downstream Deon Breaker to intercept and execute a protective halt
    with pytest.raises(Exception) as exc_info:
        await engine.run_agency_orchestrator("Execute script.")
    
    assert "Deon Circuit Breaker tripped" in str(exc_info.value)
    assert ctx.state == SystemState.CRITICAL_BREAKER_TRIPPED
