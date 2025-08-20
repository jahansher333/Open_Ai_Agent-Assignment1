from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
import os
from dotenv import load_dotenv
import chainlit as cl

load_dotenv(override=True)

my_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")
moel = os.getenv("MODEL_NAME")


external_provider = AsyncOpenAI(api_key=my_key, base_url=base_url)
Model = OpenAIChatCompletionsModel(model=moel,openai_client=external_provider)


Translater_Agent = Agent(
    name="Translater Agent",
    instructions="you are Translter Agent, you can translate text from one language to another.",
    model=Model,
)




@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content="AI Translater Assistant....").send()
    # my rompt 
    prompt = message.content
    # agent get
    result = Runner.run_sync(Translater_Agent, prompt)
    await cl.Message(content=f"Ai-response: {result.final_output}").send()