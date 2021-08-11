import cv2
import numpy as np
import youtube_dl

if __name__ == '__main__':

    #video_url = 'https://www.youtube.com/watch?v=ld1Aw4wwNIM'
    video_url = 'https://www.youtube.com/watch?v=GkzBDAaqiY4'

    ydl_opts = {}

    # create youtube-dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    # set video url, extract video information
    info_dict = ydl.extract_info(video_url, download=False)

    # get video formats available
    formats = info_dict.get('formats',None)

    for f in formats:

        # I want the lowest resolution, so I set resolution as 144p
        if f.get('format_note',None) == '144p':

            #get the video url
            url = f.get('url',None)

            # open url with opencv
            cap = cv2.VideoCapture(url)

            # check if url was opened
            if not cap.isOpened():
                print('video not opened')
                exit(-1)

            while True:
                # read frame
                ret, frame = cap.read()

                # check if frame is empty
                if not ret:
                    break

                # display frame
                cv2.imshow('frame', frame)

                if cv2.waitKey(30)&0xFF == ord('q'):
                    break

            # release VideoCapture
            cap.release()

    cv2.destroyAllWindows()
