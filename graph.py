from langgraph.graph import StateGraph, END
from langchain.prompts import ChatPromptTemplate
from llm_utils import get_gemini_model

def create_chat_graph():
    llm = get_gemini_model()
    prompt = ChatPromptTemplate.from_template("You are a helpful assistant. {user_input}")

    def generate_response(state):
        user_input = state["user_input"]
        chain = prompt | llm
        result = chain.invoke({"user_input": user_input})
        return {"response": result.content}

    # Define the LangGraph workflow
    workflow = StateGraph(dict)
    workflow.add_node("chat", generate_response)
    workflow.set_entry_point("chat")
    workflow.add_edge("chat", END)

    # Return compiled executable graph
    return workflow.compile()