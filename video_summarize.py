import os
from dotenv import load_dotenv
from langchain_community.document_loaders import YoutubeLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_community.chat_models import ChatOpenAI
from langchain.text_splitter import TokenTextSplitter

load_dotenv()

# Function to generate transcript and summary
def generate_summary(youtube_url):
    # Load Transcript
    loader = YoutubeLoader.from_youtube_url(youtube_url, language=["en", "en-US"])
    transcript = loader.load()

    # Split Transcript
    splitter = TokenTextSplitter(model_name="gpt-3.5-turbo", chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(transcript)

    # Set up LLM
    openai_api_key = openai_api_key = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo", temperature=0.3)

    # Summarize
    summarize_chain = load_summarize_chain(llm=llm, chain_type="refine", verbose=True)
    summary = summarize_chain.run(chunks)

    return summary