import cv2
import math

path='Resources/test.png'
img=cv2.imread(path)
img=cv2.resize(img,(512,512))
pointsList = []

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size=len(pointsList)
        if size!=0 and size%3 !=0:
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,255,0),2)
        cv2.circle(img,(x,y),5,(0,255,0),cv2.FILLED)
        pointsList.append([x,y])
        #print(x,y)
        print(pointsList)



def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle(pointsList):
    pt1,pt2,pt3= pointsList[-3:]
    m1=gradient(pt1,pt2)
    m2=gradient(pt1,pt3)
    angR = math.atan((m2-m1)/(1+m2*m1))
    angD = round(math.degrees(angR))
    cv2.putText(img,str(angD),(pt1[0]+40,pt1[1]),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),2)
    #print(angD)

while True:

    if len(pointsList) % 3 == 0 and len(pointsList)!=0:
        getAngle(pointsList)
    cv2.imshow('Image',img)
    cv2.setMouseCallback('Image',mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList=[]


