Explanation / Info:
 this program simulates key and mouse userinputs if a twitch viewer writes a specific message in chat
 i have just adjusted & fixed this code - i stole the most of it from here https://www.dougdoug.com/twitchplays
 controls:
   w -> press w for 2sec
   s -> press s for 2sec
   a -> press a for 2sec
   d -> press d for 2sec
   jump
   e -> press e for .7sec
   q -> press q for .7sec
   f -> press f for .7sec
   shoot -> press left mouse for 1ms
   rmb -> press right mouse for 1ms

 warnings:
  i wasnt able to test it, but i havent touched the important parts and the original works
  it keeps running until you close the command-prompt (or press the end key)
      -> it can input into every window and not just your game (-> never press crtl / windows/ alt key)
    therefore the viewers could mess with you while you have another window open (especially with mouse-keys)

I DO NOT TAKE ANY RESPONSIBILITY IF ANYTHING GOES WRONG
you can view the entire code if you rightclick and then press "edit" or "open with"->"notepad"

Setup:
 1. install python ( https://www.python.org/downloads/ )
    install python libraries for keyboard-automation (run the following lines in commandprompt)
      pip install --upgrade pyautogui
      pip install --upgrade pynput
 2. write your twitch username and oauth token into TwitchPlays-AccountInfo.py
     get token: https://twitchtokengenerator.com/
Run:
 doubleclick start.bat (on windows)
