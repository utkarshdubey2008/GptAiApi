from fastapi import FastAPI, HTTPException
from groq import Groq
from urllib.parse import unquote

app = FastAPI()

# Initialize Groq client with your API key
client = Groq(api_key="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")  # Replace with your actual key

# Define custom responses (case-insensitive matching)
custom_responses = {
    "who made you": "I am a large language model by @Thealphabotz and @AlphaApis. My creator is @Adarsh2626.",
    "who created you": "I am a large language model by @Thealphabotz and @AlphaApis. My creator is @Adarsh2626.",
    "who is your owner": "I am a large language model by @Thealphabotz and @AlphaApis. My creator is @Adarsh2626.",
    "owner name": "I am a large language model by @Thealphabotz and @AlphaApis. My creator is @Adarsh2626.",
    "name your owner": "I am a large language model by @Thealphabotz and @AlphaApis. My creator is @Adarsh2626.",
    "which model are you": "I am a large language model by @Thealphabotz and @AlphaApis. My creator is @Adarsh2626.",
    "which api you use": "I am a large language model by @Thealphabotz and @AlphaApis. My creator is @Adarsh2626."
}

@app.get("/api/gpt/chat/{prompt}")
async def chat(prompt: str):
    # URL-decode the prompt to handle spaces properly
    prompt_decoded = unquote(prompt).lower()
    
    # Check if the prompt has a custom response (case-insensitive)
    if prompt_decoded in custom_responses:
        return {"response": f"Response= {custom_responses[prompt_decoded]} Api created by @Thealphabotz and @AlphaApis."}
    
    try:
        # Create a completion with the Groq client for non-custom responses
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        # Collect the response in chunks
        response_text = ""
        for chunk in completion:
            response_text += chunk.choices[0].delta.content or ""
        
        # Format the final response with footer
        return {"response": f"{response_text} Api created by @Thealphabotz and @AlphaApis."}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
