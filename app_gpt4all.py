"""
ALSO CHECK OUT: 
# https://docs.gpt4all.io/gpt4all_python.html
# https://python.langchain.com/docs/ecosystem/integrations/gpt4all 

Langchain == 0.0.220 
gpt4all -- 0.3.6
"""


from langchain.llms import GPT4All

# Instantiate the model. Callbacks support token-wise streaming
#model = GPT4All(model="./models/gpt4all-model.bin", n_ctx=512, n_threads=8)
#model = GPT4All(model="C:\\Users\\e0513693\gpt4all\ggml-gpt4all-j-v1.3-groovy.bin", n_ctx=512, n_threads=8)
#model = GPT4All(model="ggml-gpt4all-j-v1.3-groovy.bin", n_ctx=512, n_threads=8)
#model = GPT4All(model="./ggml-gpt4all-j-v1.3-groovy.bin", n_ctx=512, n_threads=8 )

model = GPT4All(model="./ggml-gpt4all-j-v1.3-groovy.bin" )

# Generate text
response = model("Once upon a time, ")

