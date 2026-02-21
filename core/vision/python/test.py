from faceram import *
from picamera2 import Picamera2
from ethan_tracking_test import *

process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
process.communicate(input="source my-venv/bin/activate \n")
print("image sent")





try:
    cam = Picamera2()
    print("initilized cam")
    preview_config = cam.create_still_configuration(main={"size": cam.sensor_resolution})
    print("create preview config")
    cam.configure(preview_config)    
    print("configure config")

    #save to memory method (faster)    
    cam.start()
    print("camstart")
    '''
    while True:
        start_time = time.perf_counter()

        vector=locate(capture(cam))

        print(vector)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Elapsed wall-clock time: {elapsed_time:.4f} seconds")
    '''
except KeyboardInterrupt:
    cam.close()
    print("camclose")
