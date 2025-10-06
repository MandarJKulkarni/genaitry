# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        # api_key=os.environ.get("GEMINI_API_KEY"),
        api_key="GEMINI_API_KEY"
    )

    model = "gemma-3-12b-it"
    response = client.models.generate_content(
    model="gemma-3-12b-it", contents="Small joke about Software Development."
)
    # contents = [
    #     types.Content(
    #         role="user",
    #         parts=[
    #             types.Part.from_text(text="Create one liner joke about software development."),
    #         ],
    #     ),
    # ]
    # generate_content_config = types.GenerateContentConfig(
    # )

    # for chunk in client.models.generate_content_stream(
    #     model=model,
    #     contents=contents,
    #     config=generate_content_config,
    # ):
    #     print(chunk.text, end="")
    print(response.text)

if __name__ == "__main__":
    generate()
