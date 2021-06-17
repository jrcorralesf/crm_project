import os
#from os import sep

from azure.storage.fileshare import ShareServiceClient, ShareClient, ShareDirectoryClient, ShareFileClient
from azure.core.exceptions import ResourceExistsError

#constantes
connection_string = "DefaultEndpointsProtocol=https;AccountName=crminteredes;AccountKey=uy4MdNj6/Vv1tNFxdSaHC3sVqSmeuQ2Yx7pR5J3M09iE7ivG5iHQQtYYgJ9Fp5f5NJvTPN11sTnfYuA1Mi+8pQ==;EndpointSuffix=core.windows.net"
share_supply="crm-interedes"

#service = ShareServiceClient.from_connection_string(conn_str=connection_string) #conexión a la cuenta
share = ShareClient.from_connection_string(conn_str=connection_string, share_name=share_supply) #conexión al recurso compartido
#directory=ShareDirectoryClient(conn_str=connection_string, share_name=share_supply)

def upload_file(my_file,path):

    if my_file: #si hay un archivo
        path_array=os.path.normpath(path).split(os.sep)
        print('//////////////////////////////')
        print(path)
        print(path_array)
        if path_array: #si hay algo en mi lista de path
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
                
        
            file_client = ShareFileClient.from_connection_string(conn_str=connection_string, 
                                                                share_name=share_supply, 
                                                                file_path=f'{path}{my_file.name}'
                                                                )
            file_client.upload_file(my_file)

