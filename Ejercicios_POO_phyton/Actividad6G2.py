class familia:
    def init(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
        print(self.str())

    def str(self):
        hijos2 = " ".join(self.hijos)
        cadena = self.padre+" "+self.madre+" "+hijos2
        return cadena

hijos = ["Cacho", "Marto", "Santutu"]
f1 = familia("Manu", "Tolete", hijos)