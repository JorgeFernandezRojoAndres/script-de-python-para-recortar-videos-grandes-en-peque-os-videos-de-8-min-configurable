import subprocess

def cut_video(input_video, duration=480):
    # Duración de cada video cortado en segundos
    duration = duration
    output_template = "output%03d.mp4"
    # Ejecuta el comando de FFmpeg para cortar el video en segmentos de 10 minutos
    subprocess.run(["ffmpeg", "-i", input_video, "-c", "copy", "-map", "0", "-segment_time", str(duration), "-f", "segment", output_template])
    print(f"C:\\Users\\jorge\\Videos\\videoACortar.mp4 {input_video} cortado en varios archivos de {duration/60} minutos, utilizando la plantilla de nombre {output_template}")

# Nombre del video a cortar
video = "C:\\Users\\jorge\\Videos\\videoACortar.mp4"
cut_video(video)
# posibles problemas: si el ruta del archivo no aparece especificar la ruta de archivo con doble \\ , ffmpeg es una biblioteca de python que desde visual estudio se descarga con el siguiente comando pip install nombre_biblioteca, tambien es posible que el sistema pida configurar el ffmpeg Descarga la última versión de FFmpeg desde el sitio web oficial de FFmpeg.
#Descomprime el archivo descargado en una carpeta de tu elección. Por ejemplo, en "C:\ffmpeg"
#Abre el Símbolo del sistema (CMD) y escribe "setx /M PATH "C:\ffmpeg\bin"" (sin comillas) y presiona Enter.
#Reinicie su equipo para que las variables de entorno se apliquen.
#Para verificar que se instaló correctamente escriba cmd ffmpeg y si esta configurado correctamente te aparecerán las #opciones del comando ffmpeg. 
#si el error es el siguiente C:\Users\jorge>setx /M PATH "C:\ffmpeg\bin ERROR: se ha denegado el acceso a la ruta de acceso al Registro.Para solucionar este problema, debe ejecutar el comando "setx" como administrador. Puedes hacerlo abriendo el símbolo del sistema (CMD) como administrador. Haz clic con el botón derecho en el icono del símbolo del sistema y selecciona "Ejecutar como administrador". Una vez que el símbolo del sistema se abra como administrador, intente ejecutar el comando "setx" nuevamente.

#Otra opción es agregar el directorio de ffmpeg al PATH de forma temporal mediante la modificación de la variable del entorno PATH, escribiendo en el cmd:set PATH=C:\ffmpeg\bin;%PATH%
#Con esto se agrega la ruta de ffmpeg al PATH, solo para la sesión actual.

#Es importante mencionar que también es posible que existan restricciones de seguridad en tu sistema, lo que significa que es posible que no puedas mod
 