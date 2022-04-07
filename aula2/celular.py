class Celular:
    def __init__(self, numero = "", modelo = "", chip = "") -> None:
        self.numero = numero
        self.modelo = modelo
        self.chip = chip

    def __str__(self) -> str:
        return self.numero + " - " + self.modelo + " - " + self.chip
