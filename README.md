# Realtime Audio Video Sync Tool
This tool allows you to synchronise an audio and video player to circumvent audio latency caused by wireless speakers or headphones. It uses a simple workaround to fix the problem, which offers a broad range of use-cases.


## Why this project?
I used to own a Google Nest Audio stereo pair, which I wanted to use to watch movies on my laptop. However, the audio latency was so bad (almost a full second) so I couldn't use them for that. Google still hasn't fixed this and after 2 years of people complaining finally provided [a statement saying that they do not recommend using it as a TV speaker](https://www.googlenestcommunity.com/t5/Speakers-and-Displays/Terrible-delay-with-2-nest-audio-pair-with-tv/m-p/86157/highlight/true). Since I saw that a lot of people (including me) had the problem and are stuck with the speakers, I decided to create this tool.

DISCLAIMER: It is not the most practical solution, but it works for a lot of cases for me. So hopefully it works for you too.

## Who is this project for?
Anyone who has a speaker or headphone with a high audio latency and wants to watch a video on their laptop or computer in sync. I built this tool with the Google Nest Audio in mind, but it should work with any speaker that uses bluetooth or has casting functionality (syncing a casting device is explained [here](https://github.com/ArchimedesFTW/Realtime-Audio-Video-Sync-Tool#casting)).

Bear in mind that this tool is a workaround to fix the problem but  . My reasoning is that if you have a speaker with a high audio latency, you probably don't want to buy a new one.


## How it works
The concept is fairly simple and is based on the fact that the audio latency is constant. This means that if you know the audio latency, you can delay the video by the same amount of time and the audio and video will be in sync.

The tool works by playing the same video in 2 players, where you use one players as the audio source and the other as the video source. The tool will then calculate the audio latency and delay the video by the same amount of time.

As simple as this sounds, getting to play the same video in 2 players is not always as easy as it sounds. I will explain how to do this in the next section.

## How to use this tool
You

## How to use this tool in different use cases
The biggest challenge of syncing audio is not using this tool (hopefully), but playing the same video in 2 different players. Streaming services do not want you to do that, but I found a workaround for that.

Below I will list a lot of different use cases and tell you how you can use this tool in that case. If you have a use case that is not listed here and you know a solution. Please let me know and I will add it to the list.

#### Netflix (and other streaming services)
Since Netflix prevents you from watching a video in multiple tabs and it does so by checking your IP-address. You will need to perform a clever trick:

1. Get the Netflix/other streaming service application. 
2. Download the movie/video you want to watch.
3. Play the movie/video in the application offline.
4. Now open the same movie/video in your browser and use the application as the audio source and the browser as the video source or the other way around.
5. Make sure that both players their start time are set to zero (drag the slider to the start of the video and immediately press on pause).
6. Select both play buttons, and link them to the tool.
7. Press play on the tool and enjoy your movie/video in sync.

_7.1. If you want to pause the video open the tool and press the pause button. Make sure that both play buttons are at the same location ._



#### Any website on which you want to watch and play a video.
1. Open the video you want to watch in your browser.
2. Copy the link and open it in a new browser window.
3. Start both videos already, so they can buffer and play any possible adds.
4. Now open the tool and select both play buttons by pressing the right mouse button.
5. Mute the video in the browser window that you want to use as the video source.
6. Press play on the tool and enjoy your video in sync.



_**Tip** For most websites it is possible to watch a video. To do this set both videos to the 0:00 starttime, making them equal. Then, use the right arrow key to forward the video to your desired starttime in both players._


#### Youtube
Don't use this tool. There is a better more convenient tool, available here:
https://chrome.google.com/webstore/detail/youtube-audiovideo-sync/mknmhikmjljhpccebpnplhicmcfjkgbk 

You can do this by playing the same video in 2 players, where you use one players as the audio source and the other as the video source.


#### Local video files
Again, don't use this tool. VLC has a built in function for that. You can read more about it here:

https://wiki.videolan.org/VLC_HowTo/Adjust_audio_delay/ 


## Installation
```bash
pip install -r requirements.txt
python main.py
```


## Other tips

#### Casting
In order to , cast your browser tab to your chromecast and use that tab as the audio source. Your video source can be anything else. To cast your browser tab, read here:

https://support.google.com/chromecast/answer/3228332?hl=en 



#### Defeating non-constant audio latency
If you have a speaker who's latency changes everytime you start playing an video, you can make the latency constant by playing a silent audio file in the background. You can find a silent audio files here:

https://github.com/anars/blank-audio 