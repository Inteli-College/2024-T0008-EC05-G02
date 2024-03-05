import cv2
from pyzbar import pyzbar

camera = cv2.VideoCapture(0)

print("=" * 30)

print("Procurando QR code...")

while True:
    _, image = camera.read()

    barcodes = pyzbar.decode(image)

    if len(barcodes) > 0:
        break

print("QR code encontrado!")
cv2.imwrite("codigo/src/qrcodes/frame.png", image)

print("Fechando a câmera...")
camera.release()

print("Imagem salva!")
image = cv2.cvtColor(cv2.imread("frame.png"), cv2.COLOR_BGR2RGB)

decoded_text = barcodes[0].data.decode("utf-8")

print("Leitura feita:", decoded_text)
print("=" * 30)