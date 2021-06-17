import os
#from os import sep

from azure.storage.fileshare import ShareServiceClient, ShareClient, ShareDirectoryClient, ShareFileClient
from azure.core.exceptions import ResourceExistsError,ResourceNotFoundError

#constantes
connection_string = "DefaultEndpointsProtocol=https;AccountName=crminteredes;AccountKey=uy4MdNj6/Vv1tNFxdSaHC3sVqSmeuQ2Yx7pR5J3M09iE7ivG5iHQQtYYgJ9Fp5f5NJvTPN11sTnfYuA1Mi+8pQ==;EndpointSuffix=core.windows.net"
share_supply="crm-interedes"

#service = ShareServiceClient.from_connection_string(conn_str=connection_string) #conexión a la cuenta
share = ShareClient.from_connection_string(conn_str=connection_string, share_name=share_supply) #conexión al recurso compartido
#directory=ShareDirectoryClient(conn_str=connection_string, share_name=share_supply)


def download_file(path):
    try:
        if path:
            filename=os.path.basename(path)
            print('//////////////////////////////')
            print(filename)
            file_client = ShareFileClient.from_connection_string(connection_string, share_supply, path)
            dest_file_name = "DOWNLOADED-" + filename
            with open(dest_file_name, "wb") as data:
                stream = file_client.download_file()
                data.write(stream.readall())
                #stream.readinto(data)
        else:
            print("No especificó el archivo a descargar")
    except ResourceNotFoundError:
        print("Archivo no encontrado")

def upload_file(my_file,path):
    if my_file: #si hay un archivo
        if path: #si hay algo en mi lista de path
            path_array=os.path.normpath(path).split(os.sep)
            print('//////////////////////////////')
            print(path)
            print(path_array)
            try:
                share.create_directory(path_array[0])
                parent_path=path_array[0]
                path_array=path_array[1:]
                for pth in path_array:
                    sub_pht=f'{parent_path}/{pth}'
                    share.create_directory(sub_pht)
                    parent_path=sub_pht
            except ResourceExistsError:
                print("Ya existían las carpetas")
        
        azure_path = f'{path}{my_file.name}'
        file_to_upload=share.get_file_client(azure_path)
        file_to_upload.upload_file(my_file)

        #Alternativa de guardado usando el ShareFileClient
        '''file_client = ShareFileClient.from_connection_string(conn_str=connection_string, 
                                                            share_name=share_supply, 
                                                            file_path=azure_path
                                                            )
        file_client.upload_file(my_file)'''
        download_file(azure_path) #Probando


