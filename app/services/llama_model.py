from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Change this if you're using a different model
model_name = "meta-llama/Meta-Llama-3-7B-Instruct"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Send model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
