from fastapi import FastAPI
import cv2
import threading
import time
from qreader import QReader


qreader = QReader()
last_qr_data = None

def qr_code_detection():
    global last_qr_data
    cap = cv2.VideoCapture(0)  # 0 é geralmente o ID da primeira webcam detectada

    # Supondo que qreader.detect_and_decode funcione diretamente com imagens no formato do OpenCV
    while True:
        ret, img = cap.read()
        if ret:
            # Converta a imagem para RGB antes de passar para o qreader
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Atualize a chamada de acordo com a interface correta do seu qreader
            data = qreader.detect_and_decode(rgb_img)
            if data:
                last_qr_data = data[0]
                print(f"QR Code detectado: {data}")
                # break # Remova ou comente esta linha se deseja detecção contínua

        time.sleep(2)  # Pausa para não sobrecarregar o CPU
    cap.release()

# Iniciar a detecção de QR Code em uma thread separada
thread = threading.Thread(target=qr_code_detection)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/qreader/")
async def read_qr_code():
    global last_qr_data
    cap = cv2.VideoCapture(0)  # 0 é geralmente o ID da primeira webcam detectada

    # Supondo que qreader.detect_and_decode funcione diretamente com imagens no formato do OpenCV
    while True:
        ret, img = cap.read()
        if ret:
            # Converta a imagem para RGB antes de passar para o qreader
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Atualize a chamada de acordo com a interface correta do seu qreader
            data = qreader.detect_and_decode(rgb_img)
            if data:
                last_qr_data = data[0]
                print(f"QR Code detectado: {data}")
                if data[0] is not None:
                    break
        print("Tentando ler QRCODE")
        time.sleep(2)  # Pausa para não sobrecarregar o CPU
    return {"data": last_qr_data}
