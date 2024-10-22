import requests
import torch
from transformers import AutoTokenizer, ElectraForSequenceClassification, TrainingArguments, Trainer, AutoModel, AutoModelForSequenceClassification
import json


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
model = AutoModelForSequenceClassification.from_pretrained('saved_model', num_labels=2)
model.to(device)
tokenizer = AutoTokenizer.from_pretrained("beomi/KcELECTRA-base")


def get_response_letter():
    response = 'dfdfdf'
    response_json = json.dumps(response)
    python_object = json.loads(response_json)
    return python_object['content']


def sentence_predict(sent):
    model.eval()

    tokenized_sent = tokenizer(
        sent,
        return_tensors="pt",
        truncation=True,
        add_special_tokens=True,
        max_length=128
    )

    tokenized_sent.to(device)

    with torch.no_grad(): #메모리를 사용하지 않음 -> 학습이 아닌 추록을 위한 목적
        outputs = model(
            input_ids=tokenized_sent["input_ids"],
            attention_mask=tokenized_sent["attention_mask"],
            token_type_ids=tokenized_sent["token_type_ids"]
            )

    # 결과 return
    logits = outputs[0]
    logits = logits.detach().cpu()
    result = logits.argmax(-1)
    if result == 0:
        result = "0" #악성댓글
    elif result == 1:
        result = "1" #정상댓글
    return result
