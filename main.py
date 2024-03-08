from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")

client = OpenAI(api_key=config['API_KEY'])


def generateBlog(topic):
    response = client.completions.create(
        model='gpt-3.5-turbo',
        prompt="Write a paragraph about the following topic: " + topic,
        max_tokens=100,
        temperature=0.3
    )
    retrieve_blog = response.choices[0].text
    return retrieve_blog

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generateBlog(paragraph_topic))
  else:
    keep_writing = False



print(generateBlog('Python'))