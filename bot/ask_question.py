from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-nano")


def ask_question_function(sys_msg: str, hmn_msg: str) -> str:
    messages = [
        SystemMessage(content=sys_msg),
        HumanMessage(content=hmn_msg),
    ]
    result = model.invoke(messages)
    return result.content
