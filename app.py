from flask import Flask,request,jsonify,render_template
import torch,os
from transformers import T5Tokenizer,T5ForConditionalGeneration

app=Flask(__name__)

#Loading our trained model
model_path='Models/t5_grammar_correction'
tokenizer=T5Tokenizer.from_pretrained(model_path)
model=T5ForConditionalGeneration.from_pretrained(model_path)

device=torch.device("cpu")

#Defining function to correct grammar
def correct_grammar(text):
    input_text="grammar: "+text
    inputs=tokenizer.encode(input_text,return_tensors='pt').to(device)
    
    outputs=model.generate(inputs,max_length=128)
    corrected_text=tokenizer.decode(outputs[0],skip_special_tokens=True)
    
    return corrected_text

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    #Fetch input text from the form request
    input_text= next(request.form.values())
    
    #Predict and generate corrected sentence 
    corrected_text=correct_grammar(input_text)
    return render_template("index.html",corrected_text=corrected_text)
     
port=int(os.environ.get("PORT",5000)) 
#Running flask app
if __name__=="__main__":
    app.run(host="0.0.0.0",port=port,debug=True)
    
    