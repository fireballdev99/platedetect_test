import cv2

##############Import###########

path = './Image/5.jpg'
plateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
count = 0 
minArea = 1000

##############variable#############

while True:
    img = cv2.imread(path)
    # cv2.imshow("Image",img)
    # cv2.waitKey(0)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlate = plateCascade.detectMultiScale(imgGray,1.1,5)
    # Draw rectangles around the plates
    for (x, y, w, h) in numberPlate:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x-30, y-30), (x+w-5, y+h), (255, 0, 0), 2)


    # Display the output
    cv2.imshow('Detected Plates', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
