import cv2
import numpy as np
import os

frame_path = "framez/04.png"
frame = cv2.imread(frame_path)
cv2.imshow("Imagen", frame)
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()