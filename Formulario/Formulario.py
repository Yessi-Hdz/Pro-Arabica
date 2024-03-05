#Los getters y setters 

class encuesta:
    @property
    def respuestas(self):
        return self._respuestas

    @respuestas.setter
    def respuestas(self, valor):
        self._respuestas = valor

