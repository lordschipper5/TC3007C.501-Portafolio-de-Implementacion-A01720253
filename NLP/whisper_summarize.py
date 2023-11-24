import streamlit as st
import openai
import whisper

openai.api_key = 'LLAVEAPI'
model = whisper.load_model("base")


def transcribe_audio(model, file_path):
    transcript = model.transcribe(file_path)
    return transcript['text']


def CustomChatGPT(user_input):
    messages = [{"role": "system", "content": "You are an office administrator, summarize the text in key points"}]
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    return ChatGPT_reply


def main():
    st.title("Aplicación de Transcripción y Resumen de Audio")

    #Ingresar direccion del archivo de audio
    file_path = "C:/Users/lords/OneDrive/Documents/Github/TC3007C.501-Portafolio-de-Implementacion-A01720253/NLP/Whisper-ChatGPT-Audio/MA1.m4a"

    st.header("Transcripción")
    transcription = transcribe_audio(model, file_path)
    st.write(transcription)

    st.header("Resumen")
    summary = CustomChatGPT(transcription)
    st.write(summary)


if __name__ == "__main__":
    main()
