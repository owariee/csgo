# csgo
This repository contains my personal Counter-Strike: Global Offensive configuration.

## Video
- Color Mode:                       Computer Monitor
- Brightness:                       80% (1.6)
- Aspect Ratio:                     4:3 
- Resolution:                       1280x960
- Display Mode:                     Fullscreen
- Laptop Power Savings:             Disabled
 
## Advanced Video
- Global Shadow Quality:            Very Low
- Model / Texture Detail:           Low
- Texture Streaming:                Disabled
- Effect Detail:                    Low
- Shader Detail:                    Low
- Boost Player Contrast:            Enabled
- Multicore Rendering:              Enabled
- Multisampling Anti-Aliasing Mode: None
- FXAA Anti-Aliasing:               Disabled
- Texture Filtering Mode:           Bilinear
- Wait for Vertical Sync:           Disabled
- Motion Blur:                      Disabled
- Triple-Monitor Mode:              Disabled
- Use Uber Shaders:                 Auto: Enabled

## Launch Options
Copy and paste into steam launch options:
```
-novid -tickrate 128 +exec autoexec.cfg
```

## Digital Vibrance

### Windows
- VibranceGUI: 250%

### Linux
- VibrantLinux: 250%

## Installation

### Windows
1. Enter in this directory, exclude everything and then copy all .cfg files from the repo:
```
C:\Program Files(x86)\Steam\userdata\YOUR_ID3\730\local\cfg
```
Where YOUR_ID3 is your account ID3.
2. Put the launch options into CS:GO properties.
3. Install VibrantGUI and set csgo.exe executable to 250%.
4. Start CS:GO.
5. Set video settings as described before.
6. Enable developer console and set the console to be the "/" key.
7. On console, type:
```
exec autoexec
```

### Linux
1. Simply clone the repo and then:
```
STEAM_ID3=YOUR_ID3 ./install.sh
```
Where YOUR_ID3 is your account ID3.
2. Put the launch options into CS:GO properties.
3. Install VibrantLinux and set csgo_linux64 executable to be 250%.
4. Start CS:GO.
5. Set video settings as described before.
6. Enable developer console and set the console to be the "/" key.
7. On console, type:
```
exec autoexec
```

## FAQ

### What is STEAM_ID3
Steam ID3 is one of the forms that your Steam ID can appear. Steam uses it to know that some user is not another and split configurations in one folder per user per game. You can obtain it in a bunch of websites, use google to find some. It usually appears in this form:
```
[U:1:254174168]
```
But you only need the last part, like this:
```
254174168
```
By default the Linux script uses my own ID3, so it will install my config in my steam profile folder, so if you want to use this, please change the STEAM_ID3 to your account ID3 or it will simply not work.

