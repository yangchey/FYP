import torch
from transformers import MarianMTModel, MarianTokenizer
# from flask import Flask, render_template, request

model = MarianMTModel.from_pretrained("./Translation-Dzongkha-to-English/")
tokenizer = MarianTokenizer.from_pretrained("Translation-Dzongkha-to-English")


def predict(text):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    output_ids = model.generate(input_ids)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text
