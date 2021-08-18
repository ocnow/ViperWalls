import cv2
import numpy as np
import youtube_dl

if __name__ == '__main__':

    video_url = 'https://www.youtube.com/watch?v=ld1Aw4wwNIM'
    #video_url = 'https://www.youtube.com/watch?v=GkzBDAaqiY4'

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

            cap.set(cv2.CAP_PROP_POS_MSEC,832000)

            while True:
                # read frame
                ret, frame = cap.read()

                # check if frame is empty
                if not ret:
                    break

                game_shape = frame.shape
                map_frame = frame[0:int(game_shape[0]/2.4),0:game_shape[1]//4]

                b,g,r = cv2.split(map_frame)
                ret,g1 = cv2.threshold(g,177,255,cv2.THRESH_BINARY)
                ret,b1 = cv2.threshold(b,190,255,cv2.THRESH_BINARY)
                ret,r1 = cv2.threshold(r,152,255,cv2.THRESH_BINARY)

                b_not = cv2.bitwise_not(b1)
                r_not = cv2.bitwise_not(r1)

                g1_bnot = cv2.bitwise_and(g1,b_not)
                g1_brnot = cv2.bitwise_and(g1,r_not)

                cv2.imshow('game',frame)
                cv2.imshow('map',map_frame)
                cv2.imshow('viperwall',g1_brnot)
                if cv2.waitKey(30)&0xFF == ord('q'):
                    #cv2.imwrite('map_frame_image.jpg',map_frame)
                    break
            break
            # release VideoCapture
            cap.release()

    cv2.destroyAllWindows()
