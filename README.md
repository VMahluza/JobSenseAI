# 🎙️ AI Interviewer – Smart Hiring, Powered by AI  

AI Interviewer is an intelligent hiring assistant that conducts **AI-driven job interviews**, evaluates candidates, and provides recruiters with actionable insights.  

🚀 **Features:**  
✅ **AI-Generated Questions** – Dynamically tailored interview questions  
✅ **Voice-Based Q&A** – Real-time speech-to-text & AI evaluation  
✅ **Candidate Scoring** – Automated assessment based on responses  
✅ **CV & Job Matching** – AI-powered CV analysis for better hiring  
✅ **GraphQL API** – Flexible data retrieval for recruiters  

🔧 **Tech Stack:**  
- **Frontend:** Next.js (React)  
- **Backend:** Django (GraphQL API)  
- **AI Services:** LlamaIndex, ElevenLabs, Ollama  
- **Storage:** PostgreSQL, AWS S3  
- **CI/CD:** GitHub Actions  

📖 **Read the full documentation** ➡️ [README.md](./README.md)  

💻 **Get Started:**  
git clone https://github.com/your-username/ai-interviewer.git
cd ai-interviewer

# 🧠 AI Interviewer

AI Interviewer is an AI-powered system that conducts job interviews, evaluates candidates, and provides recruiters with insights.

## 🚀 Features  
- 🔹 AI-generated interview questions  
- 🎙️ Voice-based Q&A (Speech-to-Text & AI evaluation)  
- 📑 CV analysis and job matching  
- 📊 Candidate scoring and recruiter dashboard  

---

## 📜 System Architecture  

### 🏗️ **High-Level Architecture**
```mermaid
flowchart TD
    classDef frontend fill:#42A5F5,color:#fff,stroke:#1976D2
    classDef backend fill:#66BB6A,color:#fff,stroke:#388E3C
    classDef ai fill:#AB47BC,color:#fff,stroke:#7B1FA2
    classDef storage fill:#FF7043,color:#fff,stroke:#E64A19
    classDef devops fill:#FFCA28,color:#000,stroke:#F9A825

    subgraph Frontend["Frontend Layer"]
        A[Next.js UI]:::frontend
        B[Candidate Dashboard]:::frontend
        C[Recruiter Dashboard]:::frontend
        D[Interview UI]:::frontend
    end
    
    subgraph Backend["Backend Layer"]
        E[Django Backend]:::backend
        F[Authentication Service]:::backend
        G[GraphQL API Layer]:::backend
        H[Job & CV Management]:::backend
    end
    
    subgraph AIServices["AI Services"]
        I[LlamaIndex]:::ai
        J[ElevenLabs Voice Processing]:::ai
        K[Ollama Integration]:::ai
    end
    
    subgraph Storage["Storage Layer"]
        L[(PostgreSQL DB)]:::storage
        M[AWS S3 Storage]:::storage
    end
    
    subgraph DevOps["DevOps Layer"]
        N[Github Actions CI/CD]:::devops
        O[Monitoring Systems]:::devops
    end
    
    %% Core Data Flow
    A --> B & C & D
    B & C & D --> G
    G --> E
    E --> F & H
    
    %% AI Processing Flow
    E --> I & J & K
    I --> |Question Generation| E
    J --> |Voice Processing| E
    K --> |AI Integration| E
    
    %% Storage Connections
    E --> L & M
    L --> |User Data| E
    M --> |Media Files| E
    
    %% DevOps Connections
    N --> |Automated Deployment| E & G
    O --> |Monitoring| E & G

