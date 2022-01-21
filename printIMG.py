from skimage import io
import matplotlib.pyplot as plt
import os
import sys
import dlib

def main(url):
    predictor = dlib.shape_predictor("model/predictor_mydata.dat")    
    img = dlib.load_rgb_image("song.jpg")
    win = dlib.image_window(img, "Image")
    detector = dlib.get_frontal_face_detector()
    faces = detector(img)
    win.add_overlay(faces) # 얼굴 박스
    input_img = io.imread("song.jpg")
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = fig.add_subplot(111)
    ax.imshow(input_img)


    featureName = ['face', 'eyebrow1', 'eyebrow2', 'nose', 'nostril', 'eye1', 'eye2', 'lips', 'teeth']
    featureX = []
    featureY = []

    for face in faces:
        landmarks = predictor(img, face)
        parts = landmarks.parts()

        # jaw, ear to ear
        tmpX = []
        tmpY = []
        for part in parts[0:17]:
            win.add_overlay_circle(part, 3, dlib.rgb_pixel(255,0,0))
            #print("face =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            ax.plot(int(part[0]),int(part[1]),'.',color='red') 

        '''face = (329, 713) (334, 783) (344, 851) (355, 921) (376, 990) (414, 1049) (469, 1100)(534, 1137)
        (610, 1148)(684, 1135)(746, 1095)(799, 1047)(834, 989)(855, 922)(865, 855)(876, 788)(880, 722)'''
        '''[329, 334, 344, 355, 376, 414, 469, 534, 610, 684, 746, 799, 834, 855, 865, 876, 880]
         [713, 783, 851, 921, 990, 1049, 1100, 1137, 1148, 1135, 1095, 1047, 989, 922, 855, 788, 722]'''
        featureX.append(tmpX)
        featureY.append(tmpY)

        # left eyebrow
        tmpX = []
        tmpY = []
        for part in parts[17:22]:
            win.add_overlay_circle(part, 3, dlib.rgb_pixel(0, 255, 0))
            #print("left eyebrow =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            ax.plot(int(part[0]),int(part[1]),'o-',color='blue')
            '''[383, 421, 474, 529, 582] [655, 624, 615, 623, 640]'''
        featureX.append(tmpX)
        featureY.append(tmpY)


        # right eyebrow
        tmpX = []
        tmpY = []
        for part in parts[22:27]:
            win.add_overlay_circle(part, 3, dlib.rgb_pixel(0, 0, 255))
            #print("right eyebrow =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1])) 
            ax.plot(int(part[0]),int(part[1]),'.-',color='blue')
        featureX.append(tmpX)
        featureY.append(tmpY)


        # line on top of nose
        tmpX = []
        tmpY = []
        for part in parts[27:31]:
            win.add_overlay_circle(part, 3, dlib.rgb_pixel(0, 0, 0))
            #print("nose =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
        featureX.append(tmpX)
        featureY.append(tmpY)


        # bottom part of the nose
        tmpX = []
        tmpY = [] 
        for part in parts[31:36]:
            win.add_overlay_circle(part, 3, dlib.rgb_pixel(255, 0, 255))
            #print("nostril =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
        featureX.append(tmpX)
        featureY.append(tmpY)


        # left eye
        tmpX = []
        tmpY = [] 
        for part in parts[36:42]:
            win.add_overlay_circle(part, 3, dlib.rgb_pixel(255, 255, 0))
            #print("left eye =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
        featureX.append(tmpX)
        featureY.append(tmpY)

        # right eye
        tmpX = []
        tmpY = [] 
        for part in parts[42:48]:
            win.add_overlay_circle(part, 3, dlib.rgb_pixel(0, 255, 255))
            #print("right eye =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
        featureX.append(tmpX)
        featureY.append(tmpY)

        # outer part of the lips
        tmpX = []
        tmpY = [] 
        for part in parts[48:60]:
            win.add_overlay_circle(part, 3, dlib.rgb_pixel(100, 100, 100))
            #print("lips =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
        featureX.append(tmpX)
        featureY.append(tmpY)


        # inner part of the lips
        tmpX = []
        tmpY = [] 
        for part in parts[60:68]:
            win.add_overlay_circle(part, 3, dlib.rgb_pixel(255, 255, 255))
            #print("teeth =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
        featureX.append(tmpX)
        featureY.append(tmpY)

    result = [featureName,featureX,featureY]
    print(result)
    plt.savefig('_result.jpg') # 사진 점선만    
    win.wait_until_closed()
    return result

main('hi')