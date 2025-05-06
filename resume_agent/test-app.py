# Os import
import os
from dotenv import load_dotenv

# LangChain Imports
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_community.document_loaders import PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Weaviate Imports
from getpass import getpass
import weaviate
from weaviate.wcs import WCS

load_dotenv()


# Weaviate auth
my_credentials = weaviate.auth.AuthClientPassword(username=input("User name: "), password=getpass('Password: '))
my_wcs = WCS(my_credentials)

# Weaviate cluster creation
cluster_name = 'my_test_cluster'
weaviate_url = my_wcs.create(cluster_name=cluster_name)
weaviate_url
my_wcs.is_ready(cluster_name)

# Connecting to the cluster
client = weaviate.Client(weaviate_url)
client.is_ready()
