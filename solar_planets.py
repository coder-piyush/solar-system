import cv2
img = cv2.imread('solar-system.jpg')
# Sun
cv2.putText(img,
            'Sun',
            (80, 100),
            cv2.FONT_HERSHEY_COMPLEX,
            1.5,
            (0, 0, 255)
            )
# Mercury
cv2.putText(img,
            'Mercury',
            (120, 180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
# Venus
cv2.putText(img,
            'Venus',
            (190, 270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
# Earth
cv2.putText(img,
            'Earth',
            (290, 270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
# Mars
cv2.putText(img,
            'Mars',
            (390, 270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
# Jupiter
cv2.putText(img,
            'Jupiter',
            (560, 370),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
# Saturn
cv2.putText(img,
            'Saturn',
            (760, 320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
# Uranus
cv2.putText(img,
            'Uranus',
            (980, 290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
# Neptune
cv2.putText(img,
            'Neptune',
            (1120, 290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.imshow('Output', img)
cv2.waitKey(0)
