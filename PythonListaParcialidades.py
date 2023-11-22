import pandas as pd
import os

#*****
#***** Pendiente aclarar la estructura completa, Dentro de DOCUMENTOS VIGENTES, 01 PDF existen APROBADOS y RECHAZADOS
#*****

# Ruta base donde se deben verificar los subdirectorios
#ruta_base = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\01 PARCIALIDADES\\'  
ruta_base = 'R:\\01 PARCIALIDADES\\'  

# Nombre del archivo de log
archivo_log = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\PROCESO\\log.txt'

# Planilla con la lista de parcialidades
archivo_excel = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\01 PARCIALIDADES\\Listado de Parcialidades.xlsx'


# Carga el archivo Excel en un DataFrame Hoja de Parcialidades.
df = pd.read_excel(archivo_excel, sheet_name='PARCIALIDADES')

# Filtra el DataFrame para considerar solo parcialidades a 'PROCESAR' igual a 'S'
df_parcialidades = df[df['PROCESAR'] == 'S']

# Abre el archivo de log en modo de escritura
with open(archivo_log, 'w') as log_file:
    # Itera a través de cada parcialidad y la procesa
    for parcialidad in df_parcialidades['PARCIALIDAD']:
        log_file.write(f'Parcialidad: {parcialidad}\n')

        # Comprueba si existen los subdirectorios
        ruta_parcialidad = os.path.join(ruta_base, parcialidad)
        subdirectorios = ['DOCUMENTOS APROBADOS', 'DOCUMENTOS VIGENTES']

        for subdirectorio in subdirectorios:
            ruta_subdirectorio = os.path.join(ruta_parcialidad, subdirectorio)
            if not os.path.exists(ruta_subdirectorio):
                log_file.write(f"El subdirectorio '{subdirectorio}' no existe para la parcialidad '{parcialidad}'.\n")
            else:
                # Verifica la existencia de los subdirectorios en subdirectorio
                carpetas = ['01 PDF', '02 EDITABLE']

                for carpeta in carpetas:
                    ruta_carpeta = os.path.join(ruta_subdirectorio, carpeta)
                    if not os.path.exists(ruta_carpeta):
                        log_file.write(f"La carpeta '{carpeta}' del subdirectorio '{subdirectorio}' no existe para la parcialidad '{parcialidad}'.\n")
                    else:
                        if carpeta == '01 PDF':
                            ruta_carpeta_01_PDF_A = os.path.join(ruta_carpeta, 'APROBADOS')
                            if not os.path.exists(ruta_carpeta_01_PDF_A):
                                log_file.write(f"No existe carpeta APROBADOS en La carpeta '{carpeta}' del subdirectorio '{subdirectorio}' no existe para la parcialidad '{parcialidad}'.\n")

                            ruta_carpeta_01_PDF_R = os.path.join(ruta_carpeta, 'RECHAZADOS')
                            if not os.path.exists(ruta_carpeta_01_PDF_R):
                                log_file.write(f"No existe carpeta RECHAZADOS en La carpeta '{carpeta}' del subdirectorio '{subdirectorio}' no existe para la parcialidad '{parcialidad}'.\n")

print("Proceso finalizado. Los resultados se han guardado en el archivo de log.")
