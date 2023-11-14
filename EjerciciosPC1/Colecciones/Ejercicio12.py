formatos = ['.gif','.jpg','.jpeg','.png','.pdf','.txt','.zip']
print('Los formatos permitidos son los siguientes:\n ', formatos)
archivo = input('Ingrese el nombre y tipo de archivo para indicarle el MIME:\n').lower()

nom_file, extension = archivo.split('.')

mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg':'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

if extension in mime:
    print('El tipo de MIME del archivo es:\t ',mime[extension])
else: print('El tipo no está en la lista por ende el MIME es:\t application/octet-stream.')


   