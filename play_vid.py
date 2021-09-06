import cv2
import numpy as np
import youtube_dl

if __name__ == '__main__':

    #video_url = 'https://www.youtube.com/watch?v=ld1Aw4wwNIM'
    video_url = 'https://www.youtube.com/watch?v=7tYIN73gRzc'

    ydl_opts = {}

    # create youtube-dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    # set video url, extract video information
    info_dict = ydl.extract_info(video_url, download=False)

    # get video formats available
    formats = info_dict.get('formats',None)

    mapMask = cv2.imread('Images/mask_image.jpg',0)
    print(mapMask.shape)


    for f in formats:
        #print(f.get('format_note',None))
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

            while True:
                # read frame
                ret, frame = cap.read()

                game_shape = frame.shape
                map_frame = frame[0:int(game_shape[0]/2.4),30:int(game_shape[1]/4.5)]



                #print(map_frame.shape)
                mapBit = cv2.bitwise_and(map_frame,map_frame,mask =mapMask )
                #mapBit = cv2.GaussianBlur(mapBit,(2,2))
                mapHsv = cv2.cvtColor(mapBit, cv2.COLOR_BGR2HSV)
                mask1 = cv2.inRange(mapHsv, (75, 30, 60), (85, 140,200))
                target = cv2.bitwise_and(mapHsv,mapHsv, mask=mask1)
                # check if frame is empty

                low_threshold = 50
                high_threshold = 150
                edges = cv2.Canny(target, low_threshold, high_threshold)

                rho = 1  # distance resolution in pixels of the Hough grid
                theta = np.pi / 180  # angular resolution in radians of the Hough grid
                threshold = 15  # minimum number of votes (intersections in Hough grid cell)
                min_line_length = 50  # minimum number of pixels making up a line
                max_line_gap = 20  # maximum gap in pixels between connectable line segments
                line_image = np.copy(target) * 0  # creating a blank to draw lines on

                # Run Hough on edge detected image
                # Output "lines" is an array containing endpoints of detected line segments
                lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                                    min_line_length, max_line_gap)

                for line in lines:
                    for x1,y1,x2,y2 in line:
                        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

                # Draw the lines on the  image
                lines_edges = cv2.addWeighted(mapBit, 0.8, line_image, 1, 0)


                if not ret:
                    break

                # display frame
                #cv2.imshow('frame2', frame)
                #cv2.imshow('frame', mapBit)

                cv2.imshow('frame1', mapHsv)
                cv2.imshow('frame3', lines_edges)


                if cv2.waitKey(30)&0xFF == ord('q'):
                    break

            # release VideoCapture
            cap.release()

    cv2.destroyAllWindows()
