from dataclasses import dataclass

@dataclass
class ExnovaClient:
    email: str
    password: str
    mode: str = "demo"
    connected: bool = False

    def connect(self):
        if self.mode.lower() != "demo":
            raise RuntimeError("This V1 only permits DEMO mode.")
        if not self.email or not self.password:
            raise RuntimeError("Configure EXNOVA_EMAIL and EXNOVA_PASSWORD in .env")

        # IMPORTANT:
        # The public Exnova wrapper is unofficial/reverse-engineered. Do not
        # assume a documented official REST API exists. This V1 deliberately
        # does not send credentials to an undocumented endpoint.
        # The next adapter will implement the verified current WebSocket flow.
        self.connected = True
        return {
            "connected": True,
            "mode": "demo",
            "message": "Credentials loaded locally. Protocol adapter is intentionally not enabled yet."
        }

    def disconnect(self):
        self.connected = False
        return {"connected": False}

    def status(self):
        return {
            "connected": self.connected,
            "mode": self.mode,
            "trading_enabled": False,
            "credentials_configured": bool(self.email and self.password),
        }

    def account(self):
        return {
            "mode": "demo",
            "connected": self.connected,
            "note": "Account/balance retrieval will be enabled after the current Exnova protocol is verified."
        }
