
    # importing the cv2 library
import cv2
import subprocess
import time
import os
import numpy as np
# Set before importing picamera2 or initiating Picamera2()
os.environ['LIBCAMERA_LOG_LEVELS'] = '4' 
#from picamzero import Camera
from picamera2 import Picamera2

def avglocation(faces):
    
    faces = np.delete(faces, [2,3], axis=1) if len(faces)!=0 else [[1296,972]]
    faces = np.mean(faces, axis=0)
    return faces

def capture(cam):

    pic = cam.capture_array("main")
    time.sleep(0.000001)
    print("captured")

    '''
    request = cam.capture_request(flush=True)
    print("start request")
# Extract data from the 'main' buffer
    pic = request.make_array('main') 
    print("capture array")
    request.flush()
    print("flush")
# Release the request back to the system
    cam.release_request(request)
    print("release request")
    '''
    #pic = increase_brightness_hsv(pic,50)
#debug code
    #process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #process.communicate(input="scp image.jpg sham@10.78.19.181:/home/sham/Desktop/hackathonproject2026")
    #print("image sent")


    
 #   pic = np.delete(pic, 3, axis=2)    
  #  cv2.imwrite("image.jpg", pic)

    #print(pic)
    return pic


def locate(pic):
    # loading the haar case algorithm file into alg variable
    alg = "haarcascade_frontalface_default.xml"
    # passing the algorithm to OpenCV
    haar_cascade = cv2.CascadeClassifier(alg)
    # loading the image path into file_name variable - replace <INSERT YOUR IMAGE NAME HERE> with the path to your image
    # creating a black and white version of the image
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

    gray_img = cv2.cvtColor(pic, cv2.COLOR_RGB2BGR)
    
    # detecting the faces
    faces = haar_cascade.detectMultiScale(
        gray_img, scaleFactor=1.05, minNeighbors=2, minSize=(300, 300)
    )
    #storeface(faces,pic)
    print(len(faces))
    faces = avglocation(np.array(faces))



    
    #print(faces)
    #debugcode()
    return faces


def debugcode():
    process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.communicate(input="scp image.jpg sham@10.51.165.181:/home/sham/Desktop/hackathonproject2026 \n \\")
    print("image sent")

 
def storeface(faces,pic):
    i = 0
    # for each face detected
    for x, y, w, h in faces:
        # crop the image to select only the face
        cropped_image = pic[y : y + h, x : x + w]
        pos = pic[y:y+100, x: x+100]
        # loading the target image path into target_file_name variable  - replace <INSERT YOUR TARGET IMAGE NAME HERE> with the path to your target image
 #       target_file_name = '~/stored-faces/' + str(i) + '.jpg'
        target_file_name = os.path.join('stored-faces', str(i)+'.jpg')

    
        cv2.imwrite(
            target_file_name,
            cropped_image,
        )


    #debug code
        process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.communicate(input="scp stored-faces/"+str(i)+'.jpg'+" sham@10.78.19.181:/home/sham/Desktop/hackathonproject2026 \n")    
        print(str(i),"sent")        
        i = i + 1;



    
