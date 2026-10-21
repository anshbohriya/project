import cohere
import tempfile
import os
import json
from playsound import playsound
from gtts import gTTS  
# AI Brain
COHERE_API_KEY = "tnqkpwYx6ndsroLszQfOoLQOtMeJ5zVpgOdlm8kH"   
# MEMORY
def load_memory():
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=4)

# Load memory at start
memory = load_memory()

# AI Reply (Cohere)
import cohere
co = cohere.Client("tnqkpwYx6ndsroLszQfOoLQOtMeJ5zVpgOdlm8kH")

# This function makes Rukia talk back to me using AI
# I used Cohere's API here instead of OpenAI because it's faster for chat

def ai_reply(user_input):
    reply = co.chat(
        model="command-a-03-2025",
        message=user_input,
        preamble=(
           "You are Rukia, a friendly anime-style girl who speaks only in English. "
    "You must not use Japanese words or phrases. "
    "You should not use roleplay-style expressions (like *smiles* or *waves*). "
    "Speak naturally in plain English, like a cheerful anime girl."
        ),
        temperature=0.9
    )
    return reply.text


# gTTS TTS (Anime Type Girl Voice) ( text to speech )
def speak_tts(text: str):
    try:
        # gTTS defaults 
        tts = gTTS(text=text, lang="en", tld="com.au")  # softer, lighter female tone  # softer tone
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            tts.save(f.name)
            temp_path = f.name

        playsound(temp_path)
        os.remove(temp_path)
    except Exception as e:
        print(f"[TTS Error] {e}")


#  MAIN LOOP
def main():
    print("✨ Anime AI Girl is ready! (type 'exit' to quit)")

    while True:
        user = input("\nYou: ").strip()
        if user.lower() in {"exit", "quit"}:
            break

        reply = ai_reply(user)
        print(f"AI Girl: {reply}")

        speak_tts(reply)

if __name__ == "__main__":
    main()
