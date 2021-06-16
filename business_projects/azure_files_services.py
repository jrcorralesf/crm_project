from azure.storage.fileshare import ShareServiceClient, ShareClient, ShareDirectoryClient, ShareFileClient

#constantes
connection_string = "DefaultEndpointsProtocol=https;AccountName=crminteredes;AccountKey=uy4MdNj6/Vv1tNFxdSaHC3sVqSmeuQ2Yx7pR5J3M09iE7ivG5iHQQtYYgJ9Fp5f5NJvTPN11sTnfYuA1Mi+8pQ==;EndpointSuffix=core.windows.net"
share_supply="crm-interedes"

#service = ShareServiceClient.from_connection_string(conn_str=connection_string) #conexión a la cuenta
#share = ShareClient.from_connection_string(conn_str=connection_string, share_name=share_supply) #conexión al recurso compartido


def upload_file(my_file):
    
    file_client = ShareFileClient.from_connection_string(conn_str=connection_string, 
                                                        share_name=share_supply, 
                                                        file_path=my_file.name
                                                        )

    file_client.upload_file(my_file)

