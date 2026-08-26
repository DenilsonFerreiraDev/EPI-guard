import os
import bcrypt
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Configurações de Segurança
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "minha_chave_secreta_super_segura_epi_guard_2026")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    """Valida se a senha digitada corresponde ao hash salvo no banco."""
    return bcrypt.checkpw(senha_plana.encode('utf-8'), senha_hash.encode('utf-8'))


def gerar_hash_senha(senha: str) -> str:
    """Gera um hash seguro utilizando bcrypt puro."""
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return hash_bytes.decode('utf-8')


def criar_token_acesso(dados: dict, expira_delta: Optional[timedelta] = None) -> str:
    dados_copia = dados.copy()
    if expira_delta:
        expira = datetime.now(timezone.utc) + expira_delta
    else:
        expira = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    dados_copia.update({"exp": expira})
    return jwt.encode(dados_copia, SECRET_KEY, algorithm=ALGORITHM)


async def obter_usuario_atual(token: str = Depends(oauth2_scheme)):
    credenciais_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas ou token expirado.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario: str = payload.get("sub")
        if usuario is None:
            raise credenciais_exception
        return usuario
    except JWTError:
        raise credenciais_exception