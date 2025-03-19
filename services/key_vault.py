import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

"""
La variable de entorno KEY_VAULT_NAME debe contener el nombre del key vault en Azure.
La funcion get_secret obtiene el valor de un secreto almacenado en el key vault.
Para utilizar la funcion get_secret, se debe importar el modulo (from services.key_vault import get_secret) y llamar a la funcion con el nombre del secreto "get_secret("nombre_secreto")"
"""

key_vault_name = os.environ["KEY_VAULT_NAME"]
if not key_vault_name:
    raise ValueError("La variable de entorno KEY_VAULT_NAME no está definida.")

KVUri = f"https://{key_vault_name}.vault.azure.net"

credential = DefaultAzureCredential()

client = SecretClient(vault_url=KVUri, credential=credential)

def get_secret(secret_name):
    try:
        secret = client.get_secret(secret_name)
        return secret.value
    except Exception as e:
        print(f"Error al obtener el secreto '{secret_name}': {e}")
        raise
