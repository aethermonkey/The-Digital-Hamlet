import torch
from transformers import BartForConditionalGeneration, BartTokenizer, pipeline

def summarise_conversations(src_text):

    tgt_text = ""
    # So far Azma's model seems pretty good, mentioning names, and quoting items addressed.
    model_name = 'Azma-AI/bart-conversation-summarizer'
        
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    model = BartForConditionalGeneration.from_pretrained(model_name).to(torch_device)
    try:
        tokenizer = BartTokenizer(model_name)
    except:
        tokenizer = BartTokenizer.from_pretrained(model_name)    
    
    preprocessed_text = src_text.strip().replace("\n", " ")
    t5_input_text = "Summarize: " + preprocessed_text
    tokenized_text = tokenizer.encode(t5_input_text, return_tensors="pt", truncation=True, max_length=1024).to(torch_device)
    summary_ids = model.generate(tokenized_text, min_length=30, max_length=1024)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    tgt_text = summary

    return tgt_text

def sum_up(src_text, model_name, max=512, min=128, do_sample=False):
    summeriser = pipeline("summarization", model="facebook/bart-large-cnn")
    return summeriser(src_text, max_length=max, min_length=min, do_sample=do_sample)

print("--------SUMMARY--------\n")
print(sum_up(src_text,model_name))
print("-----------------------")