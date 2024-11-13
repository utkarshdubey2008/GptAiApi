from fastapi import FastAPI, HTTPException
from groq import Groq

app = FastAPI()

# Initialize Groq client with your API key
client = Groq(api_key="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")  # Replace with your actual key

# Define custom responses
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
    # Check if the prompt has a custom response
    prompt_lower = prompt.lower()
    if prompt_lower in custom_responses:
        return {"response": f"Response= {custom_responses[prompt_lower]} Api created by @Thealphabotz and @AlphaApis."}
    
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
        return {"response": f"Response= {response_text} Api created by @Thealphabotz and @AlphaApis."}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
