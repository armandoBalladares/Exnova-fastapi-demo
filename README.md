# Exnova FastAPI DEMO

V1 segura para preparar una API FastAPI para una futura integración con Exnova.

## Importante

El proyecto `exnova` disponible públicamente es un wrapper comunitario/no oficial y usa `requests` + `websocket-client`. La integración depende de un protocolo no documentado oficialmente por Exnova. Por seguridad, esta V1 **no envía todavía las credenciales a ningún endpoint no verificado ni ejecuta operaciones**.

## Requisitos

- Python 3.12 recomendado para esta prueba.
- Windows 10/11 recomendado.
- Cuenta Exnova DEMO.

## Instalación en Windows PowerShell

```powershell
cd exnova-fastapi-demo
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edita `.env` con tu cuenta DEMO:

```env
EXNOVA_EMAIL=tu_correo@ejemplo.com
EXNOVA_PASSWORD=tu_contrasena
EXNOVA_MODE=demo
```

No subas `.env` a GitHub.

## Ejecutar

```powershell
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Abre:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/broker/status

En Swagger prueba `POST /broker/connect`.

## Qué hace esta V1

- Carga credenciales desde `.env`.
- Obliga el modo `demo`.
- Expone FastAPI.
- Mantiene un adaptador separado para Exnova.
- No contiene endpoints para comprar/vender.
- No realiza trading real.

## Próxima V2

La siguiente etapa debe verificar el protocolo WebSocket actual de Exnova y, sólo después de confirmar el flujo de autenticación, implementar:

1. conexión real a DEMO;
2. sesión autenticada;
3. balance DEMO;
4. lista de activos;
5. velas/precios;
6. almacenamiento PostgreSQL;
7. paper trading;
8. pruebas automatizadas.

Nunca compartas tu contraseña aquí ni la incluyas en Git.
