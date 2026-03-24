import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

def load_document(docs_path="docs"):

    """Load all text files from the docs directory"""

    print(f"loading documents from {docs_path}")

    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"file directory {docs_path} does not exist")

    loader = DirectoryLoader(
        path=docs_path,
        glob="*.txt",
        loader_cls=TextLoader
    )

    documents = loader.load()

    if len(documents) == 0:
        raise FileNotFoundError(f"No .txt files found in {docs_path}")

    for i, doc in enumerate(documents[:2]):
        print(f"\n document {i+1}:")
        print(f" source {doc.metadata['source']}")
        print(len(doc.page_content))
        print(f"content length{doc.page_content[:100]}")
        print(doc.metadata)

    return documents

def split_documents(documents,chunk_size,chunk_overlap):

    """split documents into smaller chunkswith overlap"""
    print("splitting documents into chunks")

    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(documents)

    if chunks:
        for i, chunk in enumerate(chunks[:5]):
            print(i+1)
            print(chunk.metadata['source'])
            print(len(chunk.page_content))

            print("-" * 50)
        if len(chunks)>5:
            print(len(chunks)-5)
    return chunks


def main():
    print("Hello")
    documents = load_document(docs_path="docs")
    chunks = split_documents(documents=documents,chunk_size=800,chunk_overlap=0)


if __name__ == "__main__":
    main()
