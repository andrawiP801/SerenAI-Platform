import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from chatai.models import SiteConfig
from langdetect import detect

# No necesitas 'import openai' si ya usas langchain_openai

def get_chat(qry, session, history):
    siteconfig = SiteConfig.objects.first()
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Configuración del modelo
    model_name = siteconfig.open_ai_model if siteconfig and siteconfig.open_ai_model else "gpt-3.5-turbo-1106"
    
    llm = ChatOpenAI(
        model=model_name, 
        temperature=0.9,
        openai_api_key=api_key 
    )
    
    chat_history_for_chain = ChatMessageHistory()

    # Detectar idioma
    try:
        detected_language = detect(qry)
    except:
        detected_language = 'en'

    # Prompt base (Hardcoded como fallback seguro)
    default_prompt = """You are an emotional support assistant... (tu prompt largo)"""
    
    system_prompt = siteconfig.prompt if siteconfig and siteconfig.prompt else default_prompt

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ])

    chain = prompt | llm

    chain_with_message_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: chat_history_for_chain,
        input_messages_key="input",
        history_messages_key="chat_history",
    )
    
    msg = chain_with_message_history.invoke(
        {"input": qry}, # LangChain maneja el historial internamente con el wrapper
        {"configurable": {"session_id": session}},
    )
    
    return msg