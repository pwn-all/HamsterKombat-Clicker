# HamsterKombat Clicker
The game is like Flappy Birds once was, but with a different story. The developers ignored our attempts at communication. In the game is another set of bugs that allow you to get coins. We believe that this is disrespectful to "addicted" (in our opinion) users who "tap" all their free time.

# Steps to repeat
1. Enable `Enable webview inspecting` in `Settings`->`Advanced`->`Experimental settings`
![enter image description here](https://github.com/pwn-all/HamsterKombat-Clicker/blob/main/img/tg_settings.png?raw=true)
2. Open game, right click on page -> `Inspect` -> `Storage` and change platform to `android`
![enter image description here](https://github.com/pwn-all/HamsterKombat-Clicker/blob/main/img/platform.png?raw=true)
3. Go to `Network` tab and catch request on Tap event (`/clicker/tap`) or on Login event (`me-telegram`)
![enter image description here](https://github.com/pwn-all/HamsterKombat-Clicker/blob/main/img/token.png?raw=true)
4. Copy `Bearer` and other headers if need and replace it in script on `line 20`
```python
self.ses.headers.update({...})
```
5. Run and be free ([Video Proof](https://github.com/pwn-all/HamsterKombat-Clicker/raw/main/img/proof.mp4))

# Usage Of Script
```python
hamster = HamsterKombat(
    '17208508379891....415'  # Your Bearer Token
)
hamster.clicker()
```
