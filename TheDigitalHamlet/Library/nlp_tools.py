import torch
from transformers import BartForConditionalGeneration, BartTokenizer, pipeline
import sentencepiece as spm

model_name = 'facebook/bart-large-cnn'

src_text = """
Sure! Here's a sample chat transcript between four members of a team during a meeting:

---

Meeting Transcript: Team Brainstorming Session

Participants:
1. John - Team Leader
2. Sarah - Marketing Specialist
3. David - Developer
4. Emily - Designer

[Meeting Start]

John: Good morning, everyone! Thanks for joining today's brainstorming session. Let's dive right in. Our goal is to come up with innovative marketing strategies for our upcoming product launch. Sarah, would you like to start?

Sarah: Sure, John. I've been doing some research, and I think leveraging social media influencers could be a great way to reach our target audience. We can collaborate with popular influencers in our industry to promote our product.

David: That's an interesting idea, Sarah. We can also create a referral program to encourage our existing customers to share our product with their friends and family. This will help us leverage word-of-mouth marketing.

Emily: I agree with both Sarah and David. In addition, we should focus on creating visually appealing content for our social media platforms. Engaging videos and eye-catching graphics can help grab attention and generate interest in our product.

John: Great suggestions so far, team! Sarah, do you have any specific influencers in mind? And David, how can we track the success of the referral program?

Sarah: I've compiled a list of relevant influencers with a large following on Instagram and YouTube. I'll share the list with all of you after the meeting so we can review and narrow down our options.

David: For tracking the referral program, we can implement a unique referral code system. Each customer will receive a personalized code to share with others. When someone makes a purchase using that code, we'll be able to track it and reward the referrer accordingly.

Emily: That sounds like a solid plan, David. For the visual content, I can start working on some mockups and design templates for our social media posts. I'll make sure they align with our brand guidelines and convey the product's key features effectively.

John: Excellent, Emily! Once we have the influencer list and the referral program code system in place, we can collaborate with the influencers to create engaging content that highlights our product's unique selling points. Let's aim for a consistent and cohesive marketing campaign.

Sarah: Absolutely, John. We can also consider hosting live Q&A sessions or product demonstrations with the influencers to build trust and engage with our audience directly.

David: I like that idea, Sarah. It will give potential customers a chance to ask questions and see the product in action. We should also prepare a detailed analytics report to measure the impact of our marketing efforts and make data-driven decisions.

John: Agreed, David. Tracking and analyzing our performance will be crucial. Alright, team, let's wrap up for now. Please take the next few days to finalize the influencer list, work on the referral program implementation, and start creating the visual assets. We'll reconvene next week to discuss further. Thank you all for your valuable input today!

[Meeting End]

---

Note: This is a fictional chat transcript provided as an example. The conversation and participants can be customized to fit the specific context and objectives of the team meeting.
"""

def summarise_this(src_text):

    tgt_text = ""
    model_name = 'facebook/bart-large-cnn'
        
    # tokenizer = PegasusTokenizer.from_pretrained(model_name)
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    model = BartForConditionalGeneration.from_pretrained(model_name).to(torch_device)
    try:
        tokenizer = BartTokenizer(model_name)
    except:
        tokenizer = BartTokenizer.from_pretrained(model_name)    
    
    preprocessed_text = src_text.strip().replace("\n", " ")
    t5_input_text = "summarize meeting including names: " + preprocessed_text
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