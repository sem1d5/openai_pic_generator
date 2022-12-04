import os
import openai
import streamlit as st

openai.api_key = ("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")

# Generate the images
response = openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)

# Display the images in the app
for image in response["data"]:
  st.image(image["url"])
