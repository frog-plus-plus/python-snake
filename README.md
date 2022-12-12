
## python-snake :snake:

A recreation of the classic game "Snake" in Python with the "pygame" library.

### Here are the steps to running the game:

Step 1 - Ensure that python 3 is installed on your computer.  
You can do this by running this command in your terminal (Command Prompt/Powershell for Windows and Bash for Mac/Linux):
```
   $ python3 --version
     
     Python 3.*.*
```
If it outputs a number similar to the one above, your version of python should be able to run the game.  

__Note:__ If you use Linux, your distribution may not install pip by default with python. You should check to see if your distribution has a ```pip``` package in its repositories. For example, on Ubuntu, run ```sudo apt install python3-pip```.

Step 2 - Install ```pygame``` on your computer. You can do this by running the following command in the terminal:
```
$ python3 -m pip install pygame

[Various outputs showing the installation process]
```
__Note:__ If you are on Linux, you may need to provide root privileges using the ```sudo``` command (e.g. ```sudo python3 -m pip install pygame```)

Step 3 - Clone this git repository. Either download the project from ```github.com/frog-plus-plus/python-snake``` or, alternatively, if you have ```git``` installed, run this in your terminal in the directory of where you want to store the repository:
```
$ git clone https://github.com/frog-plus-plus/python-snake

[Various outputs showing the download process]
```

Step 4 - In a terminal, ```cd``` into the directory it downloaded into (```$ cd ./python-snake```) and run the file called ```src/main.py``` in python:
```
$ python3 src/main.py
```