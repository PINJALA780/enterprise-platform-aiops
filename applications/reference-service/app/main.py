from datetime import datetime, timezone
from typing import Optional
import logging
import uuid

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.core.config import (
    APP_NAME,
    APP_VERSION,
    APP_ENV,
)

from app.core.logging_config import configure_logging
from app.core.middleware import request_logging_middleware


# --------------------------------------------------
# APPLICATION LOGGING
# --------------------------------------------------

configure_logging()

logger = logging.getLogger("app")


# --------------------------------------------------
# FASTAPI APPLICATION
# --------------------------------------------------

app = FastAPI(
    title="Enterprise Reference Service",
    description="Reference microservice for the Enterprise Platform & AIOps project",
    version=APP_VERSION,
)

app.middleware("http")(request_logging_middleware)


# --------------------------------------------------
# TEMPORARY IN-MEMORY STORAGE
# --------------------------------------------------

orders = {}


# --------------------------------------------------
# REQUEST MODEL
# --------------------------------------------------

class OrderRequest(BaseModel):

    customer_id: str = Field(min_length=1)

    product_name: str = Field(min_length=1)

    quantity: int = Field(gt=0, le=1000)


# --------------------------------------------------
# ROOT ENDPOINT
# --------------------------------------------------

@app.get("/")
def root():

    return {
        "service": APP_NAME,
        "version": APP_VERSION,
        "status": "running"
    }


# --------------------------------------------------
# HEALTH ENDPOINT
# --------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": APP_NAME,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


# --------------------------------------------------
# READINESS ENDPOINT
# --------------------------------------------------

@app.get("/ready")
def readiness():

    return {
        "status": "ready",
        "service": APP_NAME
    }


# --------------------------------------------------
# GET ALL ORDERS
# --------------------------------------------------

@app.get("/api/v1/orders")
def get_orders():

    return {
        "count": len(orders),
        "orders": list(orders.values())
    }


# --------------------------------------------------
# CREATE ORDER
# --------------------------------------------------

@app.post("/api/v1/orders", status_code=201)
def create_order(order: OrderRequest):

    order_id = str(uuid.uuid4())

    new_order = {
        "order_id": order_id,
        "customer_id": order.customer_id,
        "product_name": order.product_name,
        "quantity": order.quantity,
        "status": "created",
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    orders[order_id] = new_order

    logger.info(
        "order_created",
        extra={
            "event": "order_created",
            "order_id": order_id,
        },
    )

    return new_order


# --------------------------------------------------
# GET ORDER BY ID
# --------------------------------------------------

@app.get("/api/v1/orders/{order_id}")
def get_order(order_id: str):

    if order_id not in orders:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return orders[order_id]


# --------------------------------------------------
# APPLICATION METADATA
# --------------------------------------------------

@app.get("/api/v1/metadata")
def metadata():

    return {
        "service": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV,
    }
