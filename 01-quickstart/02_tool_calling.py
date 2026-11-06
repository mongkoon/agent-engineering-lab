"""Step 2: Let an agent use a local order lookup tool (mock data only)."""

import asyncio
import json
import os

from agents import Agent, Runner
from agents.decorators import tool


@tool
def get_order(order_id: str) -> str:
    """Look up a mock commerce order by ID; never invent an order status."""
    orders = {"1001": {"status": "PAID"}, "1002": {"status": "SHIPPED"}}
    return json.dumps(orders.get(order_id, {"error": "NOT_FOUND"}))


async def main() -> None:
    agent = Agent(
        name="Commerce CS Agent",
        instructions=(
            "You are a Korean customer support agent. "
            "Always use get_order to answer factual order-status questions. "
            "Never invent order information. Answer in Korean."
        ),
        tools=[get_order],
        **({"model": os.environ["OPENAI_MODEL"]} if os.environ.get("OPENAI_MODEL") else {}),
    )
    result = await Runner.run(agent, "1002번 주문 상태를 알려줘.")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
