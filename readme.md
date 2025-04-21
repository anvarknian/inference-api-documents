
## **Project Description: Document Retrieval and Question Answering System (RAG)**

**Overview**:
This project is a robust document retrieval and question answering system built using **LangChain**, **Ollama**, and **Chroma** technologies. The system uses advanced natural language processing (NLP) techniques to allow users to query large datasets and retrieve answers from text documents stored in a Chroma vector database. The project is designed to handle unstructured textual data (e.g., .txt files) and offers a scalable, efficient, and flexible approach for building AI-powered question answering systems.

**How to run**:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --log-level info --reload
```

**Read the API**:

Your API will be available at:
```http://localhost:8000/docs#```

---

### **Key Features**:
1. **Document Management**:  
   The system loads, splits, and stores large volumes of text data from a specified directory. It supports handling of `.txt` files, which are loaded, split into chunks, and indexed for quick retrieval.

2. **Text Chunking & Embedding**:  
   The documents are split into smaller, manageable chunks using the **RecursiveCharacterTextSplitter**, ensuring that each chunk is small enough for efficient embedding while maintaining contextual integrity. These chunks are embedded using the **Ollama** model and stored in the **Chroma vector database** for fast similarity search.

3. **Chroma Database**:  
   **Chroma** is used as the vector store, allowing efficient storage and retrieval of document embeddings. The system ensures the vector store is built and updated dynamically as new documents are added or existing ones are modified.

4. **Question Answering (QA)**:  
   Users can input questions, and the system retrieves relevant context from the database using similarity search with relevance scores. The retrieved context is then used to generate an answer via the **Ollama** language model.

5. **API Integration**:  
   The system exposes a RESTful API built with **FastAPI**, allowing easy interaction with the document retrieval and question answering system. The API provides endpoints for querying the model and checking the system health, making it suitable for integration into larger applications or services.

6. **Health Check Endpoint**:  
   A dedicated health check endpoint is included to ensure the system is running and capable of processing queries. This feature is particularly useful for monitoring the system’s status in production environments.

7. **Logging & Monitoring**:  
   The system is equipped with logging at different levels (INFO, WARNING, ERROR) to provide insights into the application's state, including startup, shutdown, and any errors encountered during processing. Logs help with debugging, performance monitoring, and overall system observability.

---

### **Technologies Used**:
- **LangChain**: A framework for building applications that use LLMs (Large Language Models), enabling the integration of different tools for document management, question answering, and more.
- **Ollama**: A model used for generating embeddings and providing responses to queries. Ollama models are pulled and used to generate responses based on document context.
- **Chroma**: A vector database designed for storing and querying high-dimensional embeddings efficiently, enabling fast similarity search.
- **FastAPI**: A high-performance web framework used to build the RESTful API, providing endpoints for querying the system and checking its health.
- **Pydantic**: Used for data validation and defining structured data models, ensuring proper input/output handling in the API.
- **Logging**: A comprehensive logging setup is included to capture important events, errors, and performance metrics.

---

### **Use Cases**:
- **Document Search & Retrieval**: Organizations can use this system to retrieve specific information from a vast collection of documents, whether for research, compliance, or customer service purposes.
- **AI-powered Customer Support**: Integrate the system with customer support platforms to provide automated, contextually aware responses from internal documentation.
- **Knowledge Management**: Enable efficient knowledge discovery by allowing users to query a centralized repository of documents or knowledge bases.
- **Question Answering for Research**: Researchers can input queries related to their specific domains and get relevant answers from indexed research papers or technical documents.

---

### **How It Works**:
1. **Document Loading**:  
   Text documents are loaded from a specified directory using a custom `DirectoryLoader` class, which supports loading `.txt` files.

2. **Text Splitting**:  
   The documents are split into smaller chunks using the **RecursiveCharacterTextSplitter** to ensure the system handles long documents efficiently without losing context.

3. **Embedding & Storage**:  
   The text chunks are embedded using **OllamaEmbeddings** and stored in the **Chroma** vector database. This allows for fast similarity search based on vector representations of the document text.

4. **Querying**:  
   Users can send a question to the system, which will search for the most relevant document chunks using the **Chroma** database. The relevant chunks are then passed to the **Ollama** model to generate an answer, which is returned to the user.

5. **API Interface**:  
   The system provides a **RESTful API** built with **FastAPI** for easy integration into web services or applications. The API supports querying the system and checking the health of the service.

---

### **Project Structure**:
- **API Layer**: Exposes endpoints to interact with the question answering system, handle queries, and provide health status.
- **Document Management**: Responsible for loading, splitting, embedding, and saving the documents to the vector store.
- **Backend Services**: The core logic that handles querying the Chroma database, processing the results, and generating responses.
- **Logging & Monitoring**: Logs application events, errors, and performance metrics for easier debugging and monitoring.

---

### **Future Enhancements**:
- **Support for Multiple Document Formats**: Extend support to other formats like PDFs, Word docs, etc.
- **Real-time Document Updates**: Enable real-time document indexing and updating without service downtime.
- **Customizable Query Response Formatting**: Allow customization of how responses are generated, e.g., using a summary instead of a direct answer.
- **User Authentication & Authorization**: Add user authentication for secure access to the API and data.