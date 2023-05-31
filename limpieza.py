# Procedimiento para limpiar el archivo para tener las lineas completas y que sean de Venezuela
def limpiar_archivo_ven():
    # Cargtamos el archivo
    with open("../Cuentas.csv", "r", encoding='utf-8-sig') as file:
        # Cargamos el archivo donde ingresar los datos
        with open("../Cuentas-Vene.csv", "w", encoding='utf-8-sig') as file2:
            # Ingresamos el encabezado
            file2.write(next(file))
            # Recorremos el archivo
            line = ""
            for lines in file:
                line = line + lines
                if (line[len(line)-2] == '"'):
                    if (line.split('","')[7] == "VE"):
                        # Ingresamos la linea en el archivo nuevo
                        file2.write(line)
                    line = ''                    
                else:
                    line = line.replace("\n", " ")

# Procedimiento para limpiar el RIF de los cuentas
def limpiar_rif_cuentas():
    # Cargamos el archivos
    with open("../Cuentas-Vene.csv", "r", encoding='utf-8-sig') as file:
        # Cargamos el archivo donde ingresar los datos
        with open("../Cuentas-Vene-Limpio.csv", "w", encoding='utf-8-sig') as file2:
            # Archivo de error
            arch_error = open("../Cuentas-Vene-Error.csv", "w", encoding='utf-8-sig')
            # Ingresamos el encabezado
            encabezado = next(file) 
            file2.write(encabezado)
            arch_error.write(encabezado)
            # Recorremos el archivo
            for line in file:
                campos = line.split('","')
                # Limpiamos el RIF
                rif = campos[20].replace("-", "")
                # Validamos si el rif no es valido
                if ((len(rif) < 3 or (rif[0] not in "JGVE" and rif[0] not in "jgve")) and len(rif) != 0):
                    arch_error.write(line)
                else:
                    if (len(rif) != 0):
                        extension, numero = rif[0], rif[1:]
                        if (len(numero) != 9):
                            numero = "0" * (9 - len(numero)) + numero
                        rif = extension.upper() + numero
                        campos[20] = rif
                    # Validamos el codigo de pais
                    codpais = campos[8]
                    if (len(codpais) != 0):
                        if (len(codpais) == 3):
                            codpais = codpais[0:2].upper() + '-' + codpais[2]
                    campos[8] = codpais
                    # Escribimos y cambiamos la linea
                    campos = '","'.join(campos)
                    file2.write(campos)

# Programa Principal
if (__name__ == "__main__"):
    limpiar_archivo_ven()
    limpiar_rif_cuentas()
