import cv2
import numpy as np

# Cargamos la imagen y la convertimos a HSV:
cam = cv2.VideoCapture(1)

# Funcion auxiliar:
def nothing(x):
    pass

# Creamos la ventana con las trackbars:
cv2.namedWindow('Parametros')
cv2.createTrackbar('Hue Minimo', 'Parametros', 0, 179, nothing)
cv2.createTrackbar('Hue Maximo', 'Parametros', 0, 179, nothing)
cv2.createTrackbar('Saturation Minimo', 'Parametros', 0, 255, nothing)
cv2.createTrackbar('Saturation Maximo', 'Parametros', 0, 255, nothing)
cv2.createTrackbar('Value Minimo', 'Parametros', 0, 255, nothing)
cv2.createTrackbar('Value Maximo', 'Parametros', 0, 255, nothing)
cv2.createTrackbar('Kernel X', 'Parametros', 1, 30, nothing)
cv2.createTrackbar('Kernel Y', 'Parametros', 1, 30, nothing)

# Recordamos al usuario con qu� tecla se sale:
print("\nPulsa 'ESC' para salir\n")

while (1):
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Leemos los sliders y guardamos los valores de H,S,V para construir los rangos:
    hMin = cv2.getTrackbarPos('Hue Minimo', 'Parametros')
    hMax = cv2.getTrackbarPos('Hue Maximo', 'Parametros')
    sMin = cv2.getTrackbarPos('Saturation Minimo', 'Parametros')
    sMax = cv2.getTrackbarPos('Saturation Maximo', 'Parametros')
    vMin = cv2.getTrackbarPos('Value Minimo', 'Parametros')
    vMax = cv2.getTrackbarPos('Value Maximo', 'Parametros')

    # Creamos los arrays que definen el rango de colores:
    color_bajos = np.array([hMin, sMin, vMin])
    color_altos = np.array([hMax, sMax, vMax])

    print(color_bajos)
    print(color_altos)

    # Leemos los sliders que indican las dimensiones del Kernel:
    kernelx = cv2.getTrackbarPos('Kernel X', 'Parametros')
    kernely = cv2.getTrackbarPos('Kernel Y', 'Parametros')

    # Creamos el kernel:
    kernel = np.ones((kernelx, kernely), np.uint8)

    # Detectamos los colores y eliminamos el ruido:
    mask = cv2.inRange(hsv, color_bajos, color_altos)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Mostramos los resultados y salimos:
    cv2.imshow('Original', frame)
    cv2.imshow('Mascara', mask)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()