
""" Este archivo tiene la clase que imprimir el archivo html con la info de las fuentes"""

class HtmlPrinter:
    
    sources=[]
    outputfile_name="resultado.html"
    
    def __init__(self,sources) -> None:
        self.sources=sources
    
    def set_outputfile_name(self,filepath):
        self.outputfile_name=filepath
    
    def generate(self):
        html=self.generate_html_top()
        html+=self.generate_table()
        html+=self.generate_html_bottom()
        return html
        
    def save_html(self):
        html_content = self.generate()
        
        # Escribir el contenido en el archivo
        with open(self.outputfile_name, "w", encoding="utf-8") as htmlfile:
            htmlfile.write(html_content)
        
        print(f"Archivo HTML guardado como '{self.outputfile_name}'.")
    
    def generate_table(self):
        html_code=f""""""
        for row in self.sources:
            html_code+=f"""
            <tr>
                <td>{row.title}</td>
                <td><a href="{row.link}">Enlace</a></td>
                <td>{row.points_1}</td>
                <td>{row.points_2}</td>
                <td class="points_{row.result}">{row.result}</td>
            </tr>"""
        return html_code
    
    def generate_html_top(self):
        html="""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de fuentes para informe</title>
</head>
<body>
    <h1>Calculadora de recursos</h1>
    <div class="container">    
    <table>
        <thead>
            <th>Fuente</th>
            <th>Enlace</th>
            <th>Clasificación Fuente</th>
            <th>Clasificación Datos</th>
            <th>Resultado</th>
        </thead>
        <tbody>
        """
        return html
    
    def generate_html_bottom(self):
        html=f"""
        </tbody>
    </table>
    </div>
    {self.generate_css()}
</body>
</html>
        """
        return html
    
    
    def generate_css(self):
        css="""
        <style>
 body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #fff; /* Fondo blanco para impresión */
}

.container {
    max-width: 800px;
    margin: 0 auto; /* Centra horizontalmente */
    padding: 20px;
    border: 1px solid #ccc; /* Borde ligero para separación */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Sombra suave */
}

h1 {
    text-align: center;
    font-size: 1.5em;
    margin-bottom: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th, td {
    padding: 10px;
    text-align: center;
    border: 1px solid #ccc;
}

thead {
    background-color: #f0f0f0;
}

tbody tr:nth-child(even) {
    background-color: #f9f9f9;
}

.points_1 {
    background-color: #FF7F7F; /* Rojo claro */
}

.points_2 {
    background-color: #FF9999; /* Rojo */
}

.points_3 {
    background-color: #FFB3B3; /* Rojo claro */
}

.points_4 {
    background-color: #FFCCCC; /* Rojo */
}

.points_5 {
    background-color: #FFFFCC; /* Amarillo claro */
}

.points_6 {
    background-color: #DFFFDF; /* Verde claro */
}

.points_7 {
    background-color: #B3FFB3; /* Verde */
}

.points_8 {
    background-color: #99FF99; /* Verde claro */
}

.points_9 {
    background-color: #7FFF7F; /* Verde */
}

.points_10 {
    background-color: #66FF66; /* Verde brillante */
}

.link-sign {
    color: #666; /* Color gris sutil */
    text-decoration: none; /* Quitar subrayado por defecto */
    text-align: right; 
}

.link-sign:hover {
    text-decoration: underline; /* Subrayado al pasar el mouse */
}

</sytle>
        """
        return css
    
    def generate_sign(self):
        html=f"""<a class="link-sign" href="https://github.com/elanticrypt0" target="_blank">by elantycrypt0</a>"""
        return html