# Filename:retrieve_samples.py

import pylink
import socket
import sys
from random import randint
import time

HOST = '127.0.0.1'
PORT = 63565

counter = 0
timecount = 0

# connect to the tracker and open an EDF
tk = pylink.EyeLink('100.1.1.1')
tk.openDataFile('smp_test.edf')

tk.sendCommand('sample_rate 500') # set sampling rate to 1000 Hz

# make sure gaze, HREF, and raw (PUPIL) data is available over the link
tk.sendCommand('link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,INPUT')
tk.sendCommand('screen_pixel_coords = 0 0 %d %d' % (1919,1079))
tk.sendCommand('calibration_type = HV9')

# open a window to calibrate the tracker
pylink.openGraphics()
tk.doTrackerSetup()
pylink.closeGraphics()

# start recording
error = tk.startRecording(1,1,1,1)
pylink.pumpDelay(100) # cache some samples for event parsing

t_start = tk.trackerTime() # current tracker time
smp_time = -1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST,PORT))
    sock.listen()

    print('waiting for client connection')
    connection, client_address = sock.accept()

    with connection:
        print('client connected: {}'.format(client_address))

        while True:

            # break after 10 seconds have elapsed
            if tk.trackerTime() - t_start > 60000000:
                break
            
            # poll the latest samples
            dt = tk.getNewestSample()
            if dt is not None:
                if dt.isRightSample():
                    gaze = dt.getRightEye().getGaze()
                    href = dt.getRightEye().getHREF()
                    raw  = dt.getRightEye().getRawPupil()
                    pupil= dt.getRightEye().getPupilSize()
                elif dt.isLeftSample():
                    gaze = dt.getLeftEye().getGaze()
                    href = dt.getLeftEye().getHREF()
                    raw  = dt.getLeftEye().getRawPupil()
                    pupil= dt.getLeftEye().getPupilSize()

                timestamp = dt.getTime() 
                if timestamp > smp_time:

                    smp_time = timestamp
                    counter += 1
                    timecount += 10

                    x = gaze[0]/1920
                    y = gaze[1]/1080
                    pupil_left = 0.002 #in meter (2mm)
                    pupil_right = 0.002 #in meter (2mm)
                    data = ('<REC CNT="{}" TIME="{}" LPOGX="{}" LPOGY="{}" LPOGV="1" RPOGX="{}" RPOGY="{}" RPOGV="1" LPCX="0.046200" LPCY="0.927400" LPD="100" LPS="1" LPV="1" '.format(counter,timecount,x,y,x,y) +
                            'RPCX="0.406200" RPCY="0.927400" RPD="100" RPS="1.02" RPV="1" ' +
                            'LEYEX="-0.027770" LEYEY="-0.004590" LEYEX="0.63645" LPUPILD="{}" LPUPILV="1" '.format(pupil_left) +
                            'REYEX="-0.027770" REYEY="-0.004590" REYEZ="0.63645" RPUPILD="{}" RPUPILV="1" />\r\n'.format(pupil_right))

                    print('x:{} y:{}'.format(x,y))
                    connection.send(bytearray(data,'utf-8'))

    
        
tk.stopRecording() # stop recording
tk.closeDataFile() # close EDF data file on the Host
tk.close() #close the link to the tracker
