from qreader import QReader
import cv2

qreader = QReader()

camera = cv2.VideoCapture(0)

print("=" * 30)

print("Capturando imagem...")
_, image = camera.read()

print("Salvando imagem...")
cv2.imwrite("codigo/src/qrcodes/frame.png", image)

print("Fechando a câmera...")
camera.release()

print("Imagem salva!")
image = cv2.cvtColor(cv2.imread("frame.png"), cv2.COLOR_BGR2RGB)

decoded_text = qreader.detect_and_decode(image=image)

print("Leitura feita:", decoded_text)
print("=" * 30)