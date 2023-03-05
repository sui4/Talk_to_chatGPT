import openai
import asyncio

def addMessage(role, content, messages):
  messages.append({'role': role, 'content': content})

def addMessageFromUser(content, messages):
  addMessage('user', content, messages)

def addMessageFromBot(content, messages):
  addMessage('assistant', content, messages)

def parseResponseToMessage(response):
  msg = response.choices[0].message
  res = {
    'role': msg.role,
    'content': msg.content
  }
  return res

def addMessageFromResponse(response, messages):
  message = parseResponse(response)
  addMessageFromBot(message, messages)

def SendRequest(messages):
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
      temperature=0.0,
  )
  return response


async def Conversation(messages):
  # user input
  user_input = input("You: ")
  if(user_input == "exit"):
    return False
  # add user input to messages
  addMessageFromUser(user_input, messages)
  # send request
  response = SendRequest(messages)
  # response = res_mock
  botMessage = parseResponseToMessage(response)
  # add bot response to messages
  addMessage(botMessage['role'], botMessage['content'], messages)
  print("Assistant: " + botMessage['content'])

  return True
  # ask if user wants to continue
  # yn = input("Continue? (y/n): ")
  # return (yn == "y")

async def loop(messages):
  shouldContinue = await Conversation(messages)
  return shouldContinue
