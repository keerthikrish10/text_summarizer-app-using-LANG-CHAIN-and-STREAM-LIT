import subprocess

# Install langchain
subprocess.call(['pip', 'install', 'langchain'])

# Install streamlit
subprocess.call(['pip', 'install', 'streamlit'])

print("Installation completed successfully.")
import streamlit as st
from langchain_community.llms import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
