import sys
import numpy as np
import cv2


cap = cv2.VideoCapture(0)
n = 6
##ret,img=cap.read()
##cv2.imwrite('messigray.png',img)


while(1):
    ret,img=cap.read()
    #ret returns true/false on availability

    # for ()

    height, width = (600,600)
    img = cv2.resize(img,(width, height), interpolation = cv2.INTER_CUBIC)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imgGray', imgGray)

    blur = cv2.bilateralFilter(img, 9, 75, 75)
    canny = cv2.Canny(blur, 75, 200)

    dilate = cv2.dilate(canny, None, iterations=4)
    dilateInv = cv2.bitwise_not(dilate)

    cv2.imshow('canny', canny)
    cv2.imshow('dilate', dilateInv)

    rows = imgGray.shape[1]
    cols = imgGray.shape[0]
    
    X,Y,ch=img.shape
    
    for P in range(1, n + 2):
        cv2.line(img,(P*X//n,0),(P*X//n,Y),(0,255,255),2)
        
    for Q in range(1,n):
        cv2.line(img,(0,Q*Y//n),(X+150,Q*Y//n),(0,255,255),2)

    bins = []
    zeros = np.zeros((100, 100))

    for i in range(rows/100):
        for j in range(cols/100):
            vars()["bin" + str(i) + str(j)] = dilate[100*j : 100*j+100, 100*i : 100*i+100]
            vars()["binNew" + str(i) + str(j)] = dilateInv[100*j : 100*j+100, 100*i : 100*i+100]


    for i in range(rows/100):
        for j in range(cols/100):
            name = "bin" + str(i) + str(j)
            if cv2.countNonZero(vars()[name]) > 10:
                vars()["binNew" + str(i) + str(j)] = zeros
                
    name00 = vars()["binNew" + str(0) + str(0)]
    name10 = vars()["binNew" + str(0) + str(1)]
    name20 = vars()["binNew" + str(0) + str(2)]
    name30 = vars()["binNew" + str(0) + str(3)]
    name40 = vars()["binNew" + str(0) + str(4)]
    name50 = vars()["binNew" + str(0) + str(5)]
    final0 = np.concatenate((name00, name10, name20, name30, name40, name50), axis = 0)

    name01 = vars()["binNew" + str(1) + str(0)]
    name11 = vars()["binNew" + str(1) + str(1)]
    name21 = vars()["binNew" + str(1) + str(2)]
    name31 = vars()["binNew" + str(1) + str(3)]
    name41 = vars()["binNew" + str(1) + str(4)]
    name51 = vars()["binNew" + str(1) + str(5)]
    final1 = np.concatenate((name01, name11, name21, name31, name41, name51), axis = 0)

    name02 = vars()["binNew" + str(2) + str(0)]
    name12 = vars()["binNew" + str(2) + str(1)]
    name22 = vars()["binNew" + str(2) + str(2)]
    name32 = vars()["binNew" + str(2) + str(3)]
    name42 = vars()["binNew" + str(2) + str(4)]
    name52 = vars()["binNew" + str(2) + str(5)]
    final2 = np.concatenate((name02, name12, name22, name32, name42, name52), axis = 0)

    name03 = vars()["binNew" + str(3) + str(0)]
    name13 = vars()["binNew" + str(3) + str(1)]
    name23 = vars()["binNew" + str(3) + str(2)]
    name33 = vars()["binNew" + str(3) + str(3)]
    name43 = vars()["binNew" + str(3) + str(4)]
    name53 = vars()["binNew" + str(3) + str(5)]
    final3 = np.concatenate((name03, name13, name23, name33, name43, name53), axis = 0)

    name04 = vars()["binNew" + str(4) + str(0)]
    name14 = vars()["binNew" + str(4) + str(1)]
    name24 = vars()["binNew" + str(4) + str(2)]
    name34 = vars()["binNew" + str(4) + str(3)]
    name44 = vars()["binNew" + str(4) + str(4)]
    name54 = vars()["binNew" + str(4) + str(5)]
    final4 = np.concatenate((name04, name14, name24, name34, name44, name54), axis = 0)

    name05 = vars()["binNew" + str(5) + str(0)]
    name15 = vars()["binNew" + str(5) + str(1)]
    name25 = vars()["binNew" + str(5) + str(2)]
    name35 = vars()["binNew" + str(5) + str(3)]
    name45 = vars()["binNew" + str(5) + str(4)]
    name55 = vars()["binNew" + str(5) + str(5)]
    final5 = np.concatenate((name05, name15, name25, name35, name45, name55), axis = 0)
    
    final = np.concatenate((final0, final1, final2, final3, final4, final5), axis = 1)

    cv2.imshow('final', final)



    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
