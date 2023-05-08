# Realtime Audio Video Sync Tool
This tool allows you to synchronise an audio and video player to circumvent audio latency caused by wireless speakers or headphones. It uses a simple workaround to fix the problem, which offers a broad range of use-cases.


## Why this project?
I used to own a Google Nest Audio stereo pair, which I wanted to use to watch movies on my laptop. However, the audio latency was so bad (almost a full second) so I couldn't use them for that. Google still hasn't fixed this and after 2 years of people complaining finally provided [a statement saying that they do not recommend using it as a TV speaker](https://www.googlenestcommunity.com/t5/Speakers-and-Displays/Terrible-delay-with-2-nest-audio-pair-with-tv/m-p/86157/highlight/true). Since I saw that a lot of people (including me) had the problem and are stuck with the speakers, I decided to create this tool.

## Who is this project for?
Anyone who has a speaker or headphone with a high audio latency and wants to watch a video on their laptop or computer in sync. I built this tool with the Google Nest Audio in mind, but it should work with any speaker that uses bluetooth or has casting functionality (syncing a casting device is explained [here](https://github.com/ArchimedesFTW/Realtime-Audio-Video-Sync-Tool#casting)).

Bear in mind that this tool is a workaround to fix the problem but  . My reasoning is that if you have a speaker with a high audio latency, you probably don't want to buy a new one.


## How it works
The concept is fairly simple and is based on the fact that the audio latency is constant. This means that if you know the audio latency, you can delay the video by the same amount of time and the audio and video will be in sync.

The tool works by playing the same video in 2 players, where you use one player as the audio source and the other as the video source. The tool will then calculate the audio latency and delay the video by the same amount of time.

As simple as this sounds, getting to play the same video in 2 players is not always as easy as it sounds. I will explain how to do this in the next section.


## How to use this tool 

Below I will list different use cases and explain how you can use this tool in each case. If you have a use case that is not listed here and you know a solution please let me know and I will add it to the list.

### General Approach - Any website on which you want to watch and play a video.
This approach describes the general approach to use this tool. It works for most websites, but not for all. For example, it does not work for Netflix. For Netflix, need use the approach described in the next section.

1. Open the video you want to watch in your browser.
2. Copy the link and open it in a new browser window.
3. Start both videos so they can buffer and play any possible adds.
4. Now open the tool and select both play buttons by pressing the right mouse button.
5. Mute the video in the browser window that you want to use as the video source.
6. Press play on the tool and enjoy your video in sync.

_7.1. If you want to pause the video open the tool and press the pause button. Make sure that both play buttons are still at the same location._

#### Netflix and other streaming services workaround
The biggest challenge of syncing audio in netflix and other streaming services is that you can't play the same video in multiple tabs as it does so by checking your IP address. This means that you can't use the general approach described above. However, there is a workaround for this:

1. Get the Netflix/other streaming service application. 
2. Download the movie/video you want to watch.
3. Play the movie/video in the application offline.
4. Now open the same movie/video in your browser and use the application as the audio source and the browser as the video source or the other way around.
5. Make sure that both players their start time are set to zero (drag the slider to the start of the video and immediately press on pause).
6. Select both play buttons, and link them to the tool.
7. Press play on the tool and enjoy your movie/video in sync.

_7.1. If you want to pause the video open the tool and press the pause button. Make sure that both play buttons are still at the same location ._


_**Tip** For most websites it is possible to watch a video in sync without having to start to watch the video from the beginning. To do this set both videos to the 0:00 starttime, making them equal. Then, use the right arrow key to forward the video to your desired starttime in both players._


#### Youtube
Don't use this tool. There is a better more convenient tool, available here:
https://chrome.google.com/webstore/detail/youtube-audiovideo-sync/mknmhikmjljhpccebpnplhicmcfjkgbk 

You can do this by playing the same video in 2 players, where you use one players as the audio source and the other as the video source.


#### Local video files
Again, don't use this tool. VLC has a built in function for that. You can read more about it here:

https://wiki.videolan.org/VLC_HowTo/Adjust_audio_delay/ 


## Installation
You can find a zip file with the tool [here](https://github.com/ArchimedesFTW/Realtime-Audio-Video-Sync-Tool/releases).

Extract the zip and run the executable.


#### Python install

You can install run and modify the tool yourself using:
```bash
pip install -r requirements.txt
python main.py
```

It has been tested/built with python 3.11 but most other versions should work too.

## Other tips

#### Casting
If your system doesn't have bluetooth but the speaker does support audio casting, you can still use this tool. To do this, you would need to cast your browser tab to your chromecast and use that tab as the audio source. Your video source can be anything else. To cast your browser tab, read here:

https://support.google.com/chromecast/answer/3228332?hl=en 

#### Defeating non-constant audio latency
If you have a speaker who's latency changes everytime you start playing an video, you can make the latency constant by playing a silent audio file in the background. You can find a silent audio files here:

https://github.com/anars/blank-audio 
