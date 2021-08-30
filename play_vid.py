import cv2
import numpy as np
import youtube_dl

if __name__ == '__main__':

    #read mask
    mask = cv2.imread('images/breeze_map/new_map_mask.jpg')
    #video_url = 'https://www.youtube.com/watch?v=ld1Aw4wwNIM'
    #video_url = 'https://www.youtube.com/watch?v=GkzBDAaqiY4'
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

            cap.set(cv2.CAP_PROP_POS_MSEC,139000)

            while True:
                # read frame
                ret, frame = cap.read()

                # check if frame is empty
                if not ret:
                    break

                game_shape = frame.shape
                map_frame = frame[0:int(game_shape[0]/2.4),30:int(game_shape[1]/4.5)]

                #print(map_frame.shape)

                cv2.imshow('game',frame)
                cv2.imshow('map',map_frame)

                bt_and = cv2.bitwise_and(map_frame,mask)

                cv2.imshow('map2',bt_and)
                if cv2.waitKey(30)&0xFF == ord('q'):
                    #cv2.imwrite('current_map.jpg',map_frame)
                    break
            break
            # release VideoCapture
            cap.release()

    cv2.destroyAllWindows()
