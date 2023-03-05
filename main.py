import chatgpt

def main():
  # init
  apikey = "YOUR_API_KEY"
  openai.api_key = apikey
  # init end

  messages = []
  shouldContinue = True

  while(shouldContinue):
    shouldContinue = asyncio.run(loop(messages))

main()
