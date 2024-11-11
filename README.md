# DocIQ App

DocIQ is a personal document assistant application built with Streamlit. It allows users to upload PDF documents, create embeddings from the content, and interact with the documents through a chatbot powered by the Llama model. The app leverages tools like BGE embeddings and Qdrant for local vector storage.

![image](https://github.com/user-attachments/assets/ad5e4500-a5ab-4f88-83fc-2f098812d733)


## Features

- **Upload PDF Documents:** Upload documents in PDF format for processing.
- **Create Embeddings:** Use the `EmbeddingsManager` to generate embeddings from the document content.
- **Chat with Document Content:** Use the `ChatbotManager` to interact with document content through a chatbot interface.
- **Contact Section:** Get information about contributing or reaching out to the developers.

## Tech Stack

- **Streamlit** for the web interface
- **Llama 3.2** for the chatbot responses
- **BGE Embeddings** for document vectorization
- **Qdrant in local mode** for storing embeddings in a local database
- **Chroma** as a vector store to manage document embeddings

## Installation

### Prerequisites

- Python 3.8+
- `pip` for managing Python packages

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/DocIQ.git
   cd DocIQ

2. **Install Dependencies:**

Install required Python packages using pip:
`pip install -r requirements.txt`

3. **Run the App:**

Launch the Streamlit application:

`streamlit run main.py`

4. **Set Up Chroma Database:**

Ensure chroma_db directory exists as specified in the code for storing vectors. You can change this directory path in the code if desired.

### Usage
1. **Home Page:**

- View basic information about the DocIQ app and available features.
2. **Upload Document:**

- Navigate to the Chatbot page.
- Upload a PDF document using the file uploader. Once uploaded, it will display the file name and size.
3. **Create Embeddings:**

- Once a PDF is uploaded, check the Create Embeddings checkbox to generate embeddings for the document.
- The embeddings are stored locally in the Chroma database.
4. **Chat with Document:**

- After embeddings are created, interact with the document content by typing questions into the chatbot interface.
- The chatbot uses the Llama model to retrieve relevant information and respond based on the document content.
5. **Contact Us:**

- Navigate to the Contact page for information on how to contribute or contact the developers.

### Project Structure
- main.py: Contains the Streamlit application logic, including the UI setup for document upload, embedding creation, and chatbot interaction.
- chatbot.py: Defines `ChatbotManager`, which manages chatbot interactions using document embeddings and the Llama model.
- vectors.py: Defines `EmbeddingsManager`, responsible for creating embeddings from PDF content and storing them in the Chroma vector database.
- chroma_db/: Directory to store and retrieve document embeddings.
  
### Known Issues
- PDF Parsing Errors: Ensure the PDF is not encrypted and has readable text.
- Vector Store Persistence: The Chroma vector store must be correctly initialized to store and retrieve document embeddings.

### Contributing
If you'd like to contribute to DocIQ, please reach out via GitHub or email:

Email: [arthirajendran24@gmail.com](mailto:arthirajendran24@gmail.com) ✉️
GitHub: [DocIQ Repository](https://github.com/arthi-rajendran24/DocIQ.git)
