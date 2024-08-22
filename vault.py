from dotenv import load_dotenv 
import os

def load_get_secrets(secret_key: str) -> str:
    os.system('infisical export --format=dotenv-export > .env')
    load_dotenv()
    return os.getenv(secret_key)

if __name__ == '__main__':
    os.system('infisical export --format=dotenv-export > .env')
    load_dotenv()