import time
import simpleaudio as sa
import pyautogui
from pynput import mouse
import PySimpleGUI as sg


# Delay variables
delay = 0
t_start_delay = 0
calibrating = False

# UI window size
screenWidth, screenHeight = pyautogui.size()

# We indicate the play button by displaying a screenshot of the button
screenshot_size = 64


# Variable storing the position when the middle button is pressed
click_x, click_y = None, None

# The location of both the audio and play button
audio_x, audio_y = None, None
vid_x, vid_y = None, None


def start_with_delay():
    """
    Run the script.
    """
    # First move to both play buttons as some players hide the button after a while
    pyautogui.moveTo(vid_x, vid_y)
    pyautogui.moveTo(audio_x, audio_y, duration=0.5)

    # Play the audio video
    pyautogui.click()

    # Move to video button
    pyautogui.moveTo(vid_x, vid_y)

    # Wait for the delay and then click the video button.
    time.sleep(delay / 1000)
    pyautogui.click(vid_x, vid_y)
    print("Synced")


def on_click(x, y, button, pressed):
    """
    The function that's called when the middle mouse button is clicked.
    This tells us to save the position of the mouse, as the play button is located here.
    """
    global click_x, click_y

    # If you want to bind the script to a different button, change the if statement
    if button.name == "middle" and pressed:
        click_x = x
        click_y = y
        return False


def get_click_pos(name=""):
    """
    Wait for the user to click the middle mouse button and save the position.

    name: The name of the file to save a screenshot to of the click location, iff provided.

    Returns: The x and y position of the click.
    """
    # Start a thread to listen for the middle mouse button
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    global click_x, click_y

    # Wait for the user to click the middle mouse button
    listener.join()

    # Make screenshot if desired
    if len(name) > 0:
        offset = screenshot_size // 2
        print(f"{click_x}  {click_y}")
        pyautogui.screenshot(
            name + ".png",
            region=(
                click_x - offset,
                click_y - offset,
                screenshot_size,
                screenshot_size,
            ),
        )

    return click_x, click_y


def calibrate():
    """
    Calibrate the delay by playing a sound and measuring the time it takes to play.
    """
    global delay, t_start_delay, calibrating

    if not calibrating:
        calibrating = True
        t_start_delay = time.time()

        # Start thread to playsound
        wave_obj = sa.WaveObject.from_wave_file("delay_detector.wav").play()

        # Provide UI feedback
        calibrate_button.update(text="Click on the 4th beat")
    else:
        # Subtract time it takes to get to the 4th beat
        # Subtract 3 seconds + 1/8th of a second to account for the beat
        delay = int((time.time() - t_start_delay) * 1000 - 3000 - 125)

        # Negative latency means you hear the audio before the video. That is not fixable here.
        if delay < 0:
            delay = 0

        # Update delay field with the detected delay.
        delay_field.update(delay)
        calibrating = False

        # Revert buttn text to old text
        calibrate_button.update(text="Find your system's delay")


# Screen buttons
calibrate_button = sg.Button("Find your system's delay", key="calibrate")
delay_field = sg.In(size=(25, 1), enable_events=True, key="-DELAY-")
invalid_input_text = sg.Text(
    "Invalid Input", text_color="red", key="ERROR_DELAY", visible=False
)


# Create GUI
set_delay = [
    [
        sg.Text(
            "Audio and Video Syncer",
            font=("Helvetica", 18, "bold"),
        )
    ],
    [
        sg.Text(
            "Sync an audio and video player to circumvent audio latency of speakers."
        )
    ],
    # Set Delay
    [sg.Text("")],  # Empty line
    [calibrate_button],
    [sg.Text("Try to determine the delay of your system")],
    [sg.Text("")],  # Empty line
    [sg.Text("Or set it manually here:")],
    [
        sg.Text("Delay (ms)"),
        delay_field,
    ],
    # Error message on incorrect delay
    [invalid_input_text],
]

set_screens = [
    [sg.Text("Select Audio Window")],
    [sg.Image(key="audio_pos_img", size=(screenshot_size, screenshot_size))],
    [
        sg.Button("Localize Play Button", key="audio_pos_button"),
    ],
    [sg.Text("Select Video Window")],
    [sg.Image(key="vid_pos_img", size=(screenshot_size, screenshot_size))],
    [
        sg.Button("Localize Play Button", key="vid_pos_button"),
    ],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(set_delay),
        sg.VSeperator(),
        sg.Column(set_screens),
    ],
    [sg.HSeparator()],
    [
        sg.Button("Start synced play", key="play", disabled=False),
        sg.Text(
            "Select both windows!", text_color="red", key="ERROR_PLAY", visible=False
        ),
        sg.Button("Pause", key="pause", disabled=False),
    ],
]

window = sg.Window("Delay Syncer", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "calibrate" or event == sg.WIN_CLOSED:
        calibrate()

    # Check if the delay is filled in correctly
    if event == "-DELAY-":
        val = values["-DELAY-"]
        try:
            # Get list of files in folder
            delay = abs(int(val))  # TODO take time into account
            delay_field.update(delay)
            window["ERROR_DELAY"].update(visible=False)
        except:
            # window.("Invalid number")
            window["ERROR_DELAY"].update(visible=True)
            # window.AllKeysDict["ERROR_DELAY"].DisplayText = "Invalid Delay"

    elif event == "audio_pos_button":  # A file was chosen from the listbox
        window.hide()
        sg.Popup(
            "Click with the middle mouse button on the play button of player that will play the audio",
            title="Select Audio Source",
            non_blocking=True,
            button_type=sg.POPUP_BUTTONS_NO_BUTTONS,
            auto_close_duration=5,
            auto_close=True,
        )
        audio_x, audio_y = get_click_pos("audio")
        window["audio_pos_img"].update("audio.png")
        window.un_hide()

    elif event == "vid_pos_button":
        window.hide()
        sg.Popup(
            "Click with the middle mouse button on the play button of the player you want to play the video on",
            title="Select Audio Source",
            non_blocking=True,
            button_type=sg.POPUP_BUTTONS_NO_BUTTONS,
            auto_close_duration=5,
            auto_close=True,
        )
        vid_x, vid_y = get_click_pos("video")
        window["vid_pos_img"].update("video.png")
        window.un_hide()

    # If the play button is pressed, check if we have all the information we need
    # Run the sync script if we do
    elif event == "play" or event == "pause":
        if event == "pause":
            pass  # TODO make popup to ask the user still has the buttons in the correct place.

        if (audio_x is None) or (vid_x is None):
            sg.Popup(
                "Before starting playing, you need to select both an play button for the audio source and a play button for the video source",
                title="Select both sources",
                non_blocking=False,
            )
        else:
            window.minimize()
            start_with_delay()

    # Check if we filled everything correctly with this change:
    if audio_x and vid_x:
        window["play"].update(disabled=False)

window.close()
