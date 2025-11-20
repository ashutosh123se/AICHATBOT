# 🏥 Build a Complete Medical Chatbot with LLMs, LangChain, Pinecone & Flask

## 📥 STEP 01 — Clone the Repository
```bash
git clone https://github.com/ashutosh123se/AICHATBOT
```

## 🧪 STEP 02 — Create a Conda Environment
```bash
conda create -n medibot python=3.10 -y
```

Activate the environment:
```bash
conda activate medibot
```

## 📦 STEP 03 — Install the Requirements
```bash
pip install -r requirements.txt
```

## 🔐 STEP 04 — Add Environment Variables
Create a `.env` file in the project folder and add:
```bash
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENVIRONMENT=your_environment
PINECONE_INDEX_NAME=your_index_name
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_KEY=your_aws_secret_key
```

## 🧠 STEP 05 — Setup Pinecone Index
```bash
python create_pinecone_index.py
```

## 🔍 STEP 06 — Generate Embeddings for Medical Documents
```bash
python ingest.py
```

## 🚀 STEP 07 — Run the Flask Application
```bash
python app.py
```

Your app will run here:
```
http://127.0.0.1:5000
```

## 📡 API Usage

### ▶ POST /chat
Send a medical question:
```json
{
  "question": "What are the symptoms of malaria?"
}
```

### ▶ POST /upload
Upload a medical PDF document:
```
file: yourfile.pdf
```

---

## 🏗 Project Structure
```
medical-chatbot/
│
├── app.py
├── ingest.py
├── create_pinecone_index.py
├── requirements.txt
├── .env
│
├── /data
│   └── medical_docs/
│
├── /services
│   ├── embeddings.py
│   ├── llm_service.py
│   └── vector_store.py
│
└── /utils
    ├── helper.py
    └── preprocess.py
```

## 🎯 You are ready to go!
