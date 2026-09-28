import cv2
# leer la imagen con cv2 = computer vision 
img = cv2.imread('pibble.jpg')
# determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles  (640, 480, 3)   
print(img.shape)
# mostrando imagen en ventana  barra de titulo pibble 1341
cv2.imshow('pibble 1341', img)
## tiempo de espera 
cv2.waitKey(0)
# destruir todas las ventanas 
cv2.destroyAllWindows()

