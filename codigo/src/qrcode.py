import cv2
from qreader import QReader

camera = cv2.VideoCapture(1)

print("=" * 30)
print("Procurando QR code...")

qreader = QReader(model_size = 'l', min_confidence = 0.2)

while True:
    _, image = camera.read()

    decoded_text = qreader.detect_and_decode(image=image)

    if decoded_text:
        break

print("QR code encontrado!")
cv2.imwrite("qrcodes/frame.png", image)

print("Fechando a câmera...")
camera.release()

print("Imagem salva!")
image = cv2.cvtColor(cv2.imread("qrcodes/frame.png"), cv2.COLOR_BGR2RGB)

print("Leitura feita:", decoded_text)
print("=" * 30)
