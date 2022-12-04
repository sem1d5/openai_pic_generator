import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")


st.title('DALL-E image generator')

prompt = st.text_input("Enter a prompt:"
    , value = "Couple illustration in a style of Spirited Away"
    )

response = openai.Image.create(
  prompt=prompt,
  n=2,
  size="1024x1024"
)

for image in response["data"]:
  st.image(image["url"])
