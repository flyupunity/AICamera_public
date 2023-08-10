import cv2
import mediapipe as mp
import wmi
import pyautogui
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def set_volume(volume):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume_interface.SetMasterVolume(volume, None)

def set_brightness(brightness):
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)
    
def distance(pnt1, pnt2):
    return float(((pnt1[0] - pnt2[0])**2.0 + (pnt1[1] - pnt2[1])**2.0)**0.5)
    
camera = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
pyautogui.FAILSAFE = False

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

print("0) Mouse Cursor Control")
print("1) Brightness and sound control")
print("2) Brightness 2.0")
print("3) Mouse Cursor Click")

mode = int(input())

'''while mode != 0 or mode != 1:

    print("0) Mouse Cursor Control")
    print("1) Brightness and sound control")

    mode = int(input())'''

points = [[float(0) for i in range(3)] for i in range(21)]
for i in range(21):
    points[i][0] = float(0)
    points[i][1] = float(1)
    points[i][2] = False

good, img = camera.read()

if good == False:
    print("please check the camera, maybe another app is using the camera")

while good:
    
    good, img = camera.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    camera_height = img.shape[0]
    camera_width = img.shape[1]

    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
            for id, point in enumerate(handLms.landmark):
                width, height, color = img.shape
                width, height = float(point.x * height), float(point.y * width)

                points[id][0] = width
                points[id][1] = height

                if distance(points[0], points[id]) <= distance(points[0], points[id - 3]):
                    points[id][2] = False
                    
                elif distance(points[0], points[id]) > distance(points[0], points[id - 3]):
                    points[id][2] = True

            #print(results.multi_handedness[0].classification[0].label, results.multi_handedness[0].classification[0].label)
            #Brightness 2.0
            if mode == 2 and distance(points[4], points[5]) > distance(points[6], points[8]):#and results.multi_handedness[0].classification[0].label == 'Left':
                if points[8][2] == True and points[12][2] == False and points[16][2] == False and points[20][2] == False:
                    set_brightness(25)
                elif points[8][2] == True and points[12][2] == True and points[16][2] == False and points[20][2] == False:
                    set_brightness(50)
                elif points[8][2] == True and points[12][2] == True and points[16][2] == True and points[20][2] == False:
                    set_brightness(75)
                elif points[8][2] == True and points[12][2] == True and points[16][2] == True and points[20][2] == True:
                    set_brightness(100)

                    
            #Volunme
            elif mode == 1 and points[8][2] == True and points[12][2] == True and points[16][2] == False and points[20][2] == False:
                volume = height / camera_height
                if volume < 0: volume = 0
                if volume > 1: volume = 1
                
                set_volume(volume)
                #cv2.circle(img, (width, height), 15, (255, 0, 0), cv2.FILLED)
                    
            #Brightness
            elif mode == 1 and points[8][2] == True and points[12][2] == True and points[16][2] == True and points[20][2] == False:
                brightness = width / camera_width * 100
                if brightness < 1: brightness = 1
                if brightness > 100: brightness = 100
                    
                set_brightness(brightness)

            #Move cursor
            elif mode == 0 and points[8][2] == True and points[12][2] == True and points[16][2] == True and points[20][2] == True:
                    
                cursor_width = float((screen_width / camera_width) * width)
                cursor_height = float((screen_height / camera_height) * height)

                if cursor_width < 0: cursor_width = 0
                if cursor_width > screen_width: cursor_width = screen_width
                    
                if cursor_height < 0: cursor_height = 0
                if cursor_height > screen_height: cursor_height = screen_height
                pyautogui.moveTo(cursor_width, cursor_height)
                    
            #Click cursor
            elif mode == 0 and distance(points[4], points[5]) < distance(points[6], points[8]):
                pyautogui.click()
            elif mode == 3 and distance(points[4], points[5]) < distance(points[12], points[10]):
                pyautogui.click()
                

                    


    cv2.imshow("image", img)
   
    if(cv2.waitKey(1) == ord('q')):
        break

camera.release()
cv2.destroyAllWindows()

''''''

#'''left_index = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]'''
#right_middle = results.multi_hand_landmarks[1].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]'''











































