from datetime import datetime

from pydantic import BaseModel, UUID4, field_validator


class Order(BaseModel):
    """
    :market: 티커
    :side: 매수 -> bid / 매도 -> ask
    :ord_type: limit -> 지정가
    :price: 주문 가격
    :volume: 주문 수량
    :uuid: 주문 id
    """
    market: str
    side: str = 'bid'
    ord_type: str = 'limit'
    price: str
    volume: str
    # uuid: UUID4 | None = None

    @field_validator("market", mode="before")
    @classmethod
    def validate_market(cls, value: str):
        return f"KRW-{value.upper()}"

    @field_validator("price", "volume", mode="before")
    @classmethod
    def validate_price(cls, value: float):
        return str(value)


class OrderResponse(BaseModel):
    uuid: UUID4
    side: str
    ord_type: str
    price: float
    state: str
    market: str
    created_at: datetime
    volume: float
    remaining_volume: float
