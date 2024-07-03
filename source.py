""" Clase para manejar los recursos """
class Source:
    
    title=""
    link=""
    points_1=0
    points_2=0
    result=0
    
    def __init__(self,titulo,url,puntaje1,puntaje2) -> None:
        self.title=titulo.strip()
        self.link=url.strip()
        self.points_1=puntaje1.strip()
        self.points_2=puntaje2.strip()
        self.calculate()
    
    def calculate(self):
        self.result=int(self.points_1)+int(self.points_2)