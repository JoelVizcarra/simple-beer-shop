from fastapi import APIRouter, HTTPException
from api.database import get_order

router = APIRouter()

@router.get("/orders/{order_id}")
async def get_order_details(order_id: str):
    try:
        order = get_order(order_id)
        return order
    # improve error handling
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
