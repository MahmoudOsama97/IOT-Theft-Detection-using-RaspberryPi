import P3picam
import picamera
from datetime import datetime
from subprocess import call

motionState = False
picPath = "/home/pi/Desktop/cookie/images/"

def captureImage(currentTime, picPath):
    # Generate the picture's name
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
    print("We have taken a picture.")
    return picName

def getTime():
    # Fetch the current time
    currentTime = datetime.now()
    return currentTime

def timeStamp(currentTime, picPath, picName):
    # Variable for file path
    filepath = picPath + picName
    # Create message to stamp on picture
    message = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    # Create command to execute
    timestampCommand = "/usr/bin/convert " + filepath + " -pointsize 36 \
    -fill red -annotate +700+650 '" + message + "' " + filepath
    # Execute the command
    call([timestampCommand], shell=True)
    print("We have timestamped our picture.")

while True:
    motionState = P3picam.motion()
    print(motionState)
    if motionState:
        currentTime = getTime()
        picName = captureImage(currentTime, picPath)
        timeStamp(currentTime, picPath, picName)
        
