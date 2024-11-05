import hvac

# Configura la conexión a Vault
client = hvac.Client(
    url='http://localhost:8201',  # Dirección de Vault
    token='vault-distribt-token'  # Reemplaza con tu token de desarrollo
)

# Verifica que la conexión sea exitosa
if client.is_authenticated():
    print("Connected to Vault successfully.")

    # Obtén la secret
    secret_path = 'ejemplo'  # Cambia esto al path correcto
    secret = client.secrets.kv.v2.read_secret_version(path=secret_path, raise_on_deleted_version=True)

    # Imprime el contenido de la secret
    print("Secret data:", secret['data']['data'])
else:
    print("Failed to connect to Vault.")
