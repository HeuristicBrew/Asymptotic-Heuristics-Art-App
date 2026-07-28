import os
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from openai import AsyncOpenAI
from core.app_code import VariantContext, NodeTier, TripartiteEconomy, SystemState, SingularSystemEngine
from core.middleware import SystemOperationsMiddleware

class ProcessRequest(BaseModel):
    user_input: str = Field(..., min_length=1)
    node_id: str = Field(default="remote_node_01")
    tier: str = Field(default="4_percent_need_for_cognition_node")

class ProcessResponse(BaseModel):
    node_id: str
    system_state: str
    output_payload: str
    leeway_wobbles: int

app = FastAPI(title="Asymptotic Heuristics Engine API", version="2.0.0")
system_middleware = SystemOperationsMiddleware(max_allowed_wobbles=5)

def get_openai_client() -> AsyncOpenAI:
    return AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY", "mock_key"))

@app.post("/api/v1/variant/process", response_model=ProcessResponse)
async def process_variant_node_stream(request: ProcessRequest, client: AsyncOpenAI = Depends(get_openai_client)):
    if request.tier == "95_percent_baseline_node":
        tier, econ = NodeTier.LIQUIDITY_BASE, TripartiteEconomy(0.2, 0.6, 0.2)
    elif request.tier == "1_percent_structural_guardian_node":
        tier, econ = NodeTier.SOVEREIGN_PROTECTOR, TripartiteEconomy(0.5, 0.3, 0.2)
    else:
        tier, econ = NodeTier.ABSORBENT_VARIANT, TripartiteEconomy(0.6, 0.3, 0.1)

    ctx = VariantContext(node_id=request.node_id, tier=tier, economy=econ, state=SystemState.GENUINE_ROLLING)
    engine = SingularSystemEngine(context=ctx, api_client=client)

    try:
        output_result = await engine.run_agency_orchestrator(request.user_input)
    except Exception as runtime_error:
        if system_middleware.apply_leeway_protocol(ctx, runtime_error):
            return ProcessResponse(
                node_id=ctx.node_id, system_state=f"{ctx.state.name} // AUTHENTICATION:[HB-1/100-ALPHA-VOID-7]",
                output_payload=f"[Leeway Absorbed] Structural wobble caught: {str(runtime_error)}",
                leeway_wobbles=ctx.leeway_error_count
            )
        raise HTTPException(status_code=500, detail=f"Systemic Node Stall: {str(runtime_error)}")

    return ProcessResponse(
        node_id=ctx.node_id, system_state=f"{ctx.state.name} // AUTHENTICATION:[HB-1/100-ALPHA-VOID-7]",
        output_payload=output_result, leeway_wobbles=ctx.leeway_error_count
    )

if __name__ == "__main__":
    uvicorn.run("main_server:app", host="0.0.0.0", port=8000, reload=True)
