from fastapi import FastAPI
import cv2
import threading
import time
from qreader import QReader
import uvicorn
from datetime import datetime
import json
from dateutil.relativedelta import relativedelta


qreader = QReader(model_size = 'l', min_confidence = 0.3)
last_qr_data = None

def qr_code_detection():
    global last_qr_data
    cap = cv2.VideoCapture(1)  # 0 é geralmente o ID da primeira webcam detectada

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
    cap = cv2.VideoCapture(1)  # 0 é geralmente o ID da primeira webcam detectada

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
                cv2.imwrite(f"backend/qrcodes/{data[0]}.jpg", rgb_img)
                if data[0] is not None:
                    six_months_ahead = (datetime.now() + relativedelta(months=6)).strftime("%Y-%m-%d")
                    try:
                        drug_info = json.loads(data[0])
                    except json.JSONDecodeError:
                        return {"error": "Invalid QR code content"}, 400
                    # Extract information into variables
                    name = drug_info.get("Name")
                    dose = drug_info.get("Dose")
                    due_date = drug_info.get("Due date")
                    lot = drug_info.get("Lot")
                    supplier = drug_info.get("Supplier")

                    if name != "Dobutamina + Glicose 50%" or due_date < six_months_ahead:
                        return {"error": "medicamento próximo do vencimento ou não é o medicamento correto"}
                    else:
                        return {"name": name, "dose": dose, "due_date": due_date, "lot": lot, "supplier": supplier}
        print("Tentando ler QRCODE")
        time.sleep(2)  # Pausa para não sobrecarregar o CPU

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)