import time
import cv2
import PySimpleGUI as sg

SpeakingLanguages = ["English", "Spanish", "French", "German", "Italian", "Portuguese", "Russian", "Japanese", "Korean", "Chinese"]
TranslateLanguages = ["English", "Spanish", "French", "German", "Italian", "Portuguese", "Russian", "Japanese", "Korean", "Chinese"]

# Camera Settings
camera_index = 0
video_capture = cv2.VideoCapture(camera_index)

time.sleep(2.0)

# Initial window size
initial_window_width = 800
initial_window_height = 600

# Camera size
camera_width = 800
camera_height = 600

# init Windows Manager
sg.theme("DarkBlue")

# def webcam col
colwebcam1_layout = [[sg.Image(filename="", key="cam1", size=(camera_width, camera_height))]]
buttons_layout = [
    [sg.Text("Select speaking language:"), sg.Combo(SpeakingLanguages, size=(20, 100), enable_events=True, key='COMBO')],
    [sg.Text("Select translate language:"), sg.Combo(TranslateLanguages, size=(20, 100), enable_events=True, key='COMBO')]
]

buttons = sg.Column(buttons_layout, element_justification='right'), sg.VerticalSeparator()
colwebcam1 = sg.Column(colwebcam1_layout, element_justification='center')

colslayout = [colwebcam1, buttons]

layout = [colslayout]

window = sg.Window("Special Inc, Camera View", layout,
                   no_titlebar=False, alpha_channel=1, grab_anywhere=False,
                   return_keyboard_events=True, resizable=False, location=(100, 100),size=(initial_window_width, initial_window_height))

while True:
    start_time = time.time()
    event, values = window.read(timeout=20)

    if event == sg.WIN_CLOSED:
        break

    # Get camera frame
    ret, frameOrig = video_capture.read()
    if ret:
        frame = cv2.resize(frameOrig, (camera_width, camera_height))
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["cam1"].update(data=imgbytes)

video_capture.release()
cv2.destroyAllWindows()
