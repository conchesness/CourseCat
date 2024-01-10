import os

def getSecrets():
    secrets = {
        'MONGO_HOST':os.environ.get('cc_mongodb_host'),
        'MONGO_DB_NAME':'coursecat',
        'GOOGLE_CLIENT_ID': os.environ.get('cc_google_client_id'),
        'GOOGLE_CLIENT_SECRET':os.environ.get('cc_google_client_secret'),
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration"
        }
    return secrets