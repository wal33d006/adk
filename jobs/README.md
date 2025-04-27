Clone this project, create `.env` file in the root and add the following inside it:

```
# Google AI Studio
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE

# Google Cloud Vertex AI
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```
You don't directly need Vertex API in python code so you don't need to add `GOOGLE_API_KEY`