import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import sentencepiece as spm

src_text = """
In the Digital Hamlet, a vibrant community of resident agents thrives, each serving a unique purpose and collaborating to create a harmonious environment. Let's dive into a lively conversation between the bank agent, library agent, and a group of residents gathered at the town center.

Bank Agent: Good morning, everyone! I hope you're all enjoying the Digital Hamlet. I'm here to discuss some exciting news regarding our financial services. We've implemented a new system that allows seamless transactions and secure digital banking. You can now access your accounts, make transfers, and even apply for loans, all from the comfort of your virtual homes.

Library Agent: That's fantastic! As the library agent, I'm thrilled to announce that our digital library has expanded its collection. We've added a vast array of e-books, audiobooks, and educational resources. Whether you're interested in literature, self-improvement, or exploring new subjects, our digital library has something for everyone.

Resident 1: That's wonderful! I've been meaning to catch up on my reading. Thank you for the update.

Resident 2: Speaking of updates, has anyone noticed the new interactive map in the town center? It's incredibly helpful for navigating our community and discovering new places.

Bank Agent: Absolutely! The interactive map was a collaborative effort between the bank, library, and other resident agents. We wanted to provide a user-friendly tool that enhances your Digital Hamlet experience. You can easily find nearby amenities, locate events, and even connect with other residents who share similar interests.

Library Agent: And don't forget about our community events! We're planning a virtual book club where residents can gather online and discuss their favorite novels. It's a great way to foster connections and engage in meaningful conversations.

Resident 3: Count me in! I've been looking for a book club to join, and this virtual option sounds perfect.

Bank Agent: In addition to the book club, we're also organizing financial literacy workshops in collaboration with the library. We believe that empowering residents with essential financial knowledge will contribute to their overall well-being.

Resident 4: That's fantastic! I've always wanted to learn more about managing my finances effectively. These workshops will be a great opportunity for personal growth.

Library Agent: We're glad to hear that! Remember, the library is not just about books. We're here to support your lifelong learning journey and provide resources that enrich your lives in various ways.

Bank Agent: And as the bank agent, I'm here to ensure your financial needs are met securely and conveniently. If you have any questions or need assistance, please don't hesitate to reach out.

Resident 1: Thank you both for your dedication to the Digital Hamlet. It's heartwarming to see all the agents working together to create a thriving community.

Resident 2: Absolutely! The Digital Hamlet has become a place where we can learn, grow, and connect with like-minded individuals. It's a testament to the power of collaboration and technology.

As the conversation in the town center continues, the bank agent, library agent, and other resident agents continue to work hand in hand, cultivating an inclusive and enriching environment in the Digital Hamlet.

"""

def summarise_this(src_text):
    #
    #   Change for T5
    #
    tgt_text = ""
    model_name = 'google/pegasus-xsum'
    print("Model:" + model_name)
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    print(torch_device.format())
    # tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
    print("Adapter:" + str(model.device))

    model_inputs = PegasusTokenizer(src_texts=[src_text], target_texts=[tgt_text], merges_file=src_text, padding=True, truncation=True, return_tensors="pt")
    print("vocab: " + str(model_inputs.vocab_size))

    translated = model.generate(**model_inputs)

    tgt_text = PegasusTokenizer.batch_decode(translated, skip_special_tokens=True)

    return tgt_text

print(summarise_this(src_text))