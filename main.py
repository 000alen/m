from modeling_t5 import T5ForConditionalGeneration
from transformers import T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained("google/t5-v1_1-small")
