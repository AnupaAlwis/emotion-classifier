# from flask import Flask, render_template, request, redirect, url_for
# from werkzeug.utils import secure_filename
# import os


from flask import Flask, render_template, request, redirect, url_for
from preprossesor import resize_image, convert_to_grayscale, get_prediction
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(url_for('index'))

    image = request.files['image']
    if image.filename == '':
        return redirect(url_for('index'))

    # Perform emotion detection on the image here
    #Convert to 48 x 48
    resize = resize_image(image, size=(48, 48))
    
    #convert to gray scale
    grayscale = convert_to_grayscale(resize)
    
    prediction = get_prediction(grayscale)
    
    
    
    result = "Happy"  # Replace this with actual emotion detection logic

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


#==================================V2===========================================
# app = Flask(__name__)

# data = dict()
# emotions = []

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     data['emotion'] = emotion
#     return render_template('index.html', data=data)


# @app.route('/upload', methods=['POST'])
# def upload():
#     if request.method == 'POST':
#         if 'image' in request.files:
#             image = request.files['image']
#             if image.filename != '':
#                 image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename))
#                 image.save(image_path)
                
#                 # Here, you'd typically call your ML model to analyze the image
#                 # For example:
#                 # sentiment = analyze_image(image_path)
                
#                 # Dummy sentiment for the example
#                 sentiment = 'Happy'
#                 data['emotion'] = sentiment
#                 return redirect(url_for('index'))
#     return redirect(url_for('index'))














# UPLOAD_FOLDER = 'static/uploads/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     sentiment = ''
#     if request.method == 'POST':
#         data['emotion'] = emotion
#         # # Save the uploaded image
#         # if 'image' in request.files:
#         #     image = request.files['image']
#         #     if image.filename != '':
#         #         image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename))
#         #         image.save(image_path)
                
#         #         # Here, you'd typically call your ML model to analyze the image
#         #         # For example:
#         #         # sentiment = analyze_image(image_path)
                
#         #         # Dummy sentiment for the example
#         #         sentiment = 'Happy'
    
#     return render_template('index.html', sentiment=sentiment)

# if __name__ == '__main__':
#     app.run(debug=True)
