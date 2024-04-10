from fastapi import FastAPI
import cv2
import threading
import time
from qreader import QReader
import uvicorn
from datetime import datetime
import json
from dateutil.relativedelta import relativedelta

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5000",  # Permitir CORS para este site
    # Adicione outros sites se necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
device_port = '/dev/ttyUSB0' # ESCOLHE A PORTA DEPENDENDO valeu

try:
    dobot = Dobot(port=device_port)
except Exception as e:
    print(f"Error connecting to Dobot: {e}")
    dobot = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/qreader/")
def read_qr_code():
    print('funcao read qr code chamada')
    # drug_name: str, drug_dose:str):
    cap = cv2.VideoCapture(1)  # 0 é geralmente o ID da primeira webcam detectada
    # Supondo que qreader.detect_and_decode funcione diretamente com imagens no formato do OpenCV
    while True:
        ret, img = cap.read()
        if ret:
            # Converta a imagem para RGB antes de passar para o qreader
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Atualize a chamada de acordo com a interface correta do seu qreader
            data = qreader.detect_and_decode(rgb_img)
            if data and data[0] is not None:
                drug_info = json.loads(data[0])  
                print(f"QR Code detectado: {data}")
                print(drug_info)
                if drug_info is not None:
                    cv2.imwrite(f"backend/qrcodes/{drug_info.get('Nome')}.jpg", rgb_img)
                    six_months_ahead = (datetime.now() + relativedelta(months=6)).strftime("%Y-%m-%d")
                    try:
                        name = drug_info.get("Nome")
                        dose = drug_info.get("Dose")
                        due_date = datetime.strptime(drug_info.get("Data de validade"), "%d/%m/%Y").strftime("%Y-%m-%d")
                        lot = drug_info.get("Lote")
                        supplier = drug_info.get("Fornecedor")
                        # if name == drug_name and due_date > six_months_ahead and dose == drug_dose:
                        if due_date > six_months_ahead:
                            print(name,six_months_ahead, due_date, dose)
                            return({"nome": name, "validade": due_date, "dose": dose, "lote": lot, "fornecedor": supplier, "status": "em conformidade"})
                        # elif name == drug_name and due_date < six_months_ahead and dose == drug_dose:
                        else:
                            print(name,six_months_ahead, due_date, dose)
                            return({"nome": name, "validade": due_date, "dose": dose, "lote": lot, "fornecedor": supplier, "status": "vencido"})
                        # elif name == drug_name and due_date > six_months_ahead and dose != drug_dose:
                        #     print(name,six_months_ahead, due_date, dose, drug_dose)
                        #     return("dose incorreta")
                        # else:
                        #     print(name,six_months_ahead, due_date, dose, drug_dose)
                        #     return("medicamento invalido")
                    except json.JSONDecodeError:
                        return {"error": "Invalid QR code content"}, 400
                    # Extract information into variables
        print("Tentando ler QRCODE")
        time.sleep(2)  # Pausa para não sobrecarregar o CPU
@app.get("/activateTool/")
async def activate_tool():
    if dobot is not None:
        try:
            # This is a placeholder for the actual command to activate the tool.
            # Adjust this according to your tool and the pydobot documentation.
            dobot.suck(True)  # Replace 'activate_tool' with the actual method name
            return {"message": "Tool activated successfully"}
        except Exception as e:
            return {"error": f"Failed to activate tool: {e}"}
    else:
        return {"error": "Dobot is not connected"}
@app.get("/deactivateTool/")
async def deactivate_tool():
    if dobot is not None:
        try:
            # This is a placeholder for the actual command to deactivate the tool.
            # Adjust this according to your tool and the pydobot documentation.
            dobot.suck(False)  # Replace 'deactivate_tool' with the actual method name
            return {"message": "Tool deactivated successfully"}
        except Exception as e:
            return {"error": f"Failed to deactivate tool: {e}"}
    else:
        return {"error": "Dobot is not connected"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)