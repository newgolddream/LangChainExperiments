# LangChain Experiments

## Setup simple Langchain ToolChain

- install conda if necessary, create and activate a new environment
- run `pip install -r requirements.txt`
- download the mistral7b-instruct quantized model from HuggingFace (4-bit works well enough on low-powered machines)
  https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/blob/main/mistral-7b-instruct-v0.2.Q4_0.gguf
- in config.yml update MODEL_BIN_PATH to point to the model you just downloaded
- run `python main.py`

Two tests will be performed. You can run them on an Intel CPU only, but it will be slow to respond. Better to run it on an M1 or M2 where you have some GPU available. There the reasoning flows reasonably well, with iterations on the prompt shown every few seconds.

Test #1: The first will prompt the model to ask for Barack Obama's birthday. Because this answer may not appear in the base model (it does, but we ignore the fact here) Langchain call on tools you defined to research the question from the Internet. While it reasons it calls wikipedia and duckduckgo to supply it context.

Test #2: The prompt asks for Obama's age. It reasons in the same way as Test #1. But, this is a more elaborate test of reasoning since it asks for an age which is factored on a birth date in the past and now.

Sometimes it arrives at an answer. Sometimes it fails. I'm still researching how to achieve a reliable result. A local 4-bit LLM has some limitations, for one, context length. Which is why I truncate responses from wikipedia and duckduckgo to 128 chars. 

There is supoort for openAI calls in the code but I've commented them out.  On my personal openAI acct, I was getting rate limited.

When I have the time I will install an LLM on cloud, wrap an API around this script and tweak more -- with a more powerful GPU I can run the full model and I'm sure I can achieve better results.
