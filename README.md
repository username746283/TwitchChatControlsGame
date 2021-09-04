# Twitch Chat Controls Game
## Credits:
This Project is Based on DougDougs Project ( https://www.dougdoug.com/twitchplays )  
i have just updated it to python 3 (it didn't work anymore) and added an "cancel / exit" key
## Disclaimer
THIS SOFTWARE IS PROVIDED  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE ) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
## tutorial
### install:

**__Install Python__**  

1. download Python https://www.python.org/downloads/
2. run the downloaded installer
3. install dependencies
  1. open command-prompt
  2. run ```pip install --upgrade pyautogui```
  3. run ```pip install --upgrade pynput```

**__Download this__**

1. Press the green "Code" Button
2. Select "Download ZIP"
3. unzip the downloaded file into a folder

### Setup
1. Create a Twitch oAuth Token (example generator: https://twitchtokengenerator.com/) and copy it
2. open TwitchPlays_AccountInfo.py with a text editor and replace the things written in caps-lock with your twitch name and the token you just generated
3. (**LINUX ONLY**) run ```chmod +x start.sh``` in the directory

### Run
1. **On Windows:** doubleclick ```start.bat``` (if you have no fileendings: the one with the gear wheels)  
  **On Linux:** run the ```start.sh```
2. press your exit key to select it (if you press it this will immediately stop)
3. switch your window to the game

**Warning:** this simulates keyboard inputs -> it can affect more than the game (including ctrl, alt and win shortcuts)

### use (as twitch-chat)
just type what you want to do.  
default commands:
- w
- a
- s
- d
- jump
- attack (left mouse button)
- rmb (right mouse button)
- e
- q
- f
