from google import genai
from google.genai import types
from secret import api_key
# Only run this block for Google AI API
client = genai.Client(api_key=api_key)

main_image = 'screen.png'
solve_image = "image.png"
mime_type = 'image/png'

instructor = """The image one is the main challenge type, if the challenge type  in the second image matching the  type in the main image do this task (Solve this captcha challenge and send the answer in format [1, 0,..] 1 = yes, 0 = no, just send the answer no extra talking), 
if the challenge type in  the second image is not matching the type  in the main image just send  the number (0)."""

with open(main_image, 'rb') as f:
  image_bytes = f.read()

for chunk in client.models.generate_content_stream(
    model='gemini-1.5-flash',
    contents=[
      'What is this image about?',
      types.Part.from_bytes(
        data=image_bytes,
        mime_type=mime_type
      )
    ],
):
  print(chunk.text)