"""Step 1: A minimal conversational agent (requires OPENAI_API_KEY)."""

import asyncio
import os

from agents import Agent, Runner


async def main() -> None:
    agent = Agent(
        name="CS Basics Tutor",
        instructions="Explain basic customer service concepts clearly in Korean.",
        **({"model": os.environ["OPENAI_MODEL"]} if os.environ.get("OPENAI_MODEL") else {}),
    )
    result = await Runner.run(agent, "What is an order cancellation policy?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
