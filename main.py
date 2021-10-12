import datetime
from playsound import playsound
import threading

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


userInput = input("Enter the target time: ")



def Background():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(-10.0, None)
    print("Task started...")
    print(f"Alarm wil play at {userInput}")
    while True:
        time = datetime.datetime.now().strftime('%I:%M %p')
        if time == userInput:
            playsound('sound.mp3')
        else:
            pass

if __name__ == "__main__":
    threading.Thread(name='background', target=Background).start()