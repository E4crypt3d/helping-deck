# Voice Assistant using Python
This is a simple Voice Assistant program made using Python. The program can perform various tasks like opening Google, playing music, opening websites, searching on Wikipedia, and more.
## Getting Started
To get started with this program, you need to follow the steps given below:
### Prerequisites
- Python 3.x
- SpeechRecognition module
- pyttsx3 module
- wikipedia module
To install these modules, run the following commands in your terminal/command prompt:
```
pip install SpeechRecognition
pip install pyttsx3
pip install wikipedia
```
## Installation
1. Clone the repository:
```git clone https://github.com/E4crypt3d/helping-deck.git```
2. Navigate to the project directory:
```cd helping-deck```
3. Run the program:
```python assistant.py```
## Usage
The Voice Assistant can perform the following tasks:

- Searching on Wikipedia
- Opening Google, YouTube, Stack Overflow, websites, etc.
- Playing music
- Exiting the program
- To use the assistant, simply speak out the command you want it to perform. The program uses the SpeechRecognition module to convert your speech into text, and then performs the necessary actions.
## Configuration
The assistant can be configured to perform specific tasks based on your preferences. The configuration options can be found in the ```config.json``` file.

To configure the assistant, you can modify the following options in the ```"config.json"``` file:

- ```"music_playlist"```: Set the URL of your preferred music playlist on a website like YouTube.
- ```"your_website"```: Set the URL of your personal website or blog.
- ```"vscode_path"```: Set the file path to the Visual Studio Code executable on your system.
- ```"sublime_path"```: Set the file path to the Sublime Text executable on your system.


Make sure to save any changes you make to the ```"config.json"``` file. The assistant will use these configurations to perform specific tasks such as opening your preferred music playlist, your website, or your preferred text editor.
