import torch
from transformers import BartForConditionalGeneration, BartTokenizer, pipeline


def sum_up(src_text, model_name, max=512, min=128, do_sample=False):
    summeriser = pipeline("summarization", model=model_name)
    return summeriser(src_text, max_length=max, min_length=min, do_sample=do_sample)

# with open("plan/product_owner_plan.md") as f:
#     print (sum_up(f.read(), "Azma-AI/bart-conversation-summarizer", do_sample=True))
