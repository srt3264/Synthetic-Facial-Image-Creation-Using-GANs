This is two ways of building emotion classification model:
- Train on a pre-trained model like VGG
- Finetune a hugging face model :Vision Transformer (base-sized model) https://huggingface.co/google/vit-base-patch16-224-in21k



This repository contains the code for training a ResNet18 model on a custom dataset Fer2013 using PyTorch.  

The best model I saved here has :  

Train Loss: 0.960147514348662, Val Loss: 1.0336924475444929, Val Acc: 0.6544 

 At the end of this notebook , i create a pipline to use this model for any images.  
 
 Change the image_path to the images you would like to test
 ```
 # Load the model and predict the emotion for an image
model_path = 'best_model_res.pth'
image_path = 'archive/train/angry/Training_3908.jpg'
model = load_model(model_path)
input_batch = preprocess_image(image_path)
predicted_emotion = predict_emotion(model, input_batch)

print("Predicted emotion:", predicted_emotion)
 ```
