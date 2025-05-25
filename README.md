# GenAI_Mini_Project
In times of natural disasters (floods, earthquakes, wildfires, etc.), quick access to reliable information and guidance can save lives. This project uses Gemini API for real-time Q&amp;A and summarization, Vertex AI for custom intent classification, and Streamlit to provide an intuitive, interactive UI.
 Key Features:
Real-Time Crisis Assistant (via Gemini API):

Users ask questions like:

“What should I do during an earthquake?”

“Where is the nearest relief camp?”

Gemini provides accurate, contextual, and empathetic answers.

Image Analysis (optional - Vision API / Vertex AI):

Upload an image (e.g., flooded street or collapsed building).

Get damage assessment using pre-trained Vision models.

Voice Input & Multilingual Support (Vertex AI + Gemini):

Speak a query (via browser/microphone input).

Real-time transcription and Gemini-powered multilingual answer.

Emergency Summary Mode (Gemini API):

Summarize local alerts, Twitter posts, or RSS feeds into actionable insights.

Streamlit Dashboard:

Clean, mobile-first UI with:

Chat window (Gemini Q&A)

| Component       | Tech                                     |
| --------------- | ---------------------------------------- |
| Backend Logic   | Vertex AI, Gemini API                    |
| Frontend        | Streamlit or Firebase Web App            |
| Image Detection | Vertex AI Vision (optional)              |
| Voice Input     | Web Speech API + Gemini (text output)    |
| Hosting         | Cloud Run / Streamlit Sharing / Firebase |
| Data Sources    | Crisis news APIs / RSS feeds             |

What You'll Demonstrate:
Prompt engineering and Gemini API usage

Vertex AI: model deployment or pre-trained usage

Real-time Q&A and summarization

Streamlit dashboard creation

Integration of multimodal inputs (optional)

🧪 Optional Enhancements:
Alert push via Firebase Cloud Messaging

Google Maps integration for shelter locations

Crowd-sourced data tagging for image uploads
