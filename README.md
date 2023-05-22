# Accessible Gaming Keypad

The Accessible Gaming Keypad is a Python-based program designed to provide an interactive, user-friendly virtual keyboard interface for gaming. It is specifically tailored towards enhancing accessibility and can be used in a range of application scenarios.

## Configuration

The program operates based on a configuration file, `config.json`, which allows for the customization of button layout, functionality, and properties of the application window.

### Buttons

The `buttons` field in the configuration file consists of an array of button objects. Each object defines a unique virtual button on the interface.

A button object includes:
- `keys`: a string or array of strings specifying the key(s) associated with the button.
- `position`: a pair of integers indicating the button's position in the interface.
- `script`: an optional script to be executed when the button is pressed. The script is defined in the `scripts` section of the configuration file.

### Scripts

The `scripts` field defines a set of actions to be taken when a button is pressed. Each script consists of an array of action objects. 

An action object includes:
- `action`: a string indicating the type of action ("press" or "release").
- `keys`: a string or array of strings specifying the key(s) involved in the action.
- `delay`: an optional delay time (in milliseconds) between each action in the script.

### Window

The `window` field defines the properties of the application window:
- `window_height`: the height of the window.
- `window_width`: the width of the window.
- `window_x`: the x-coordinate of the window's top-left corner.
- `window_y`: the y-coordinate of the window's top-left corner.

## Running the Program

To run the program, ensure that Python and the required libraries (Tkinter, pynput, and win32gui) are installed. Then execute the Python script in your terminal.

---
=======
# AccessibleGamingKeypad
Provides a user-friendly virtual keyboard interface for gaming, enabling users to interact with games in a barrier-free and immersive manner.