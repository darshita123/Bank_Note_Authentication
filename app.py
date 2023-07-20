from flask import Flask, request
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model (1).pkl')

@app.route('/')
def welcome():
    return "Welcome to the API"

@app.route('/authenticate', methods=['GET'])
def authenticate():
    # Extract the data from the query parameters
    variance = float(request.args.get('variance'))
    skewness = float(request.args.get('skewness'))
    curtosis = float(request.args.get('curtosis'))
    entropy = float(request.args.get('entropy'))

   # Prepare the input for model prediction
    input_data = [[variance, skewness, curtosis, entropy]]

   # Use the loaded model for prediction
    result = model.predict(input_data)


    if(result == [1]):
        return "note is authenticated"

    else:
        return "note is not authenticated"

if __name__ == '__main__':
    app.run(debug=True,port=5000)


               #it is docker 

               
#docker exec <container_id/name> command (it will execute the command which you r giving for execution without moving inside the container)
#docker exec -it <container_id/name> bin/bash (for moving inside the container)
#if you want to build your own image then you will have to create a text file that is known as dockerfile.
#docker build -t <image_name> . (it will create the image based on your dockerfile)
#docker pull <image from docker hub) (it will pull the image from docker hub)
#docker start <container_name> it will start the container
#docker stop ...  stop the container
#docker run -it --name <container_name> <image_name> (it will create and start the container and run the image automatically)
#docker ps (it shows all the running containers)
#docker ps -a(it shows every containers)
#docker images(images show krta h)
#docker rm -f <container_name> (it removes all the containers  )
#docker rmi -f <image_name> (it removes all the images)


#docker push - it pushes the image into docker hub

#syntax of image name
#username/image-name:tag

