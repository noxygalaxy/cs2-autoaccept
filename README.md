# AUTOACCEPT | Counter-Strike 2
made simple enough, just tries to find specific color in specific coordinates :3

works only for 1920x1080 ( in future i will update this :p soo people with 2k, 4k dw! )

## Installation
1. Install [Python 3.X](https://www.python.org/) if you haven't already
2. Install source code and run `install.bat` ( it's gonna download required libraries! )
3. After console closed, run `start.bat` ( it's gonna start main program!)

## How does the program work?
1. After you start program by steps above ⬆️ it gonna show up window with text: "Trying to find 'ACCEPT' button..."
2. Open CS2 and start searching for match ( keep cs2 opened, don't minimize it or etc. keep it active window )
3. Then app gonna accept your match by itself!

## Change Time of accepting match
it's simple! just change time.sleep value in line 38

```
if current_color == target_color:
    time.sleep(4)
    pyautogui.click(*coordinates)
```
