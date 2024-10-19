# -*- coding: utf-8 -*-
"""Support Technician Helper Oct 19, 2024, 3_08_55 PM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YGoK3nKTGwbnzpIhmh27HZ-GJPdp9IeJ

1. Install the Vertex AI SDK: Open a terminal window and enter the command below. You can also [install it in a virtualenv](https://googleapis.dev/python/aiplatform/latest/index.html)
"""

!pip install --upgrade google-cloud-aiplatform

"""2. Use the following code in your application to request a model response"""

import base64
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting, Part


def multiturn_generate_content():
    vertexai.init(project="qwiklabs-gcp-03-a33317bb843a", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-002",
        system_instruction=[textsi_1]
    )
    chat = model.start_chat()
    print(chat.send_message(
        ["""My computer is so slow! What should I do?"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))

textsi_1 = """Your name is Roy.
You are a support technician of an IT department.
You are here to support the users with their queries."""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

multiturn_generate_content()