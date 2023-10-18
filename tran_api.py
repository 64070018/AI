try:
    import torch
except ImportError:
    import subprocess
    subprocess.call(['pip', 'install', 'torch'])

from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-th-en"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

input_text = "Your input text in Thai here."
inputs = tokenizer(input_text, return_tensors="pt")

translation = model.generate(**inputs)
translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)



app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    input_text = request.args.get('text')
    print(input_text)

    # if 'text' not in data:
    #     return jsonify({'error': 'The "text" field is missing in the request data.'}), 400

    # input_text = data

    inputs = tokenizer(input_text, return_tensors="pt")
    translation = model.generate(**inputs)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)

    return jsonify({'translation': translated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)