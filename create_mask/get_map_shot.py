import cv2
import numpy as np
import youtube_dl


video_url = 'https://www.youtube.com/watch?v=7tYIN73gRzc'

ydl_opts = {}

# create youtube-dl object
ydl = youtube_dl.YoutubeDL(ydl_opts)

# set video url, extract video information
info_dict = ydl.extract_info(video_url, download=False)

# get video formats available
formats = info_dict.get('formats',None)

for f in formats:

    # I want the lowest resolution, so I set resolution as 144p
    if f.get('format_note',None) == '1080p60':

        #get the video url
        url = f.get('url',None)

        # open url with opencv
        cap = cv2.VideoCapture(url)

        # check if url was opened
        if not cap.isOpened():
            print('video not opened')
            exit(-1)

        cap.set(cv2.CAP_PROP_POS_MSEC,844000)

        ret, frame = cap.read()
        game_shape = frame.shape
        map_frame = frame[0:int(game_shape[0]/2.4),30:int(game_shape[1]/4.5)]

        cv2.imshow('cur_map',map_frame)
        cv2.imwrite('map_shot.jpg',map_frame)
        cv2.waitKey(0)
        break
