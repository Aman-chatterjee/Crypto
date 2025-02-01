import os
from fastapi import HTTPException, Header
import jwt

secret_key = os.getenv('SECRET_KEY')
if not secret_key:
    raise RuntimeError("SECRET_KEY environment variable is not set!")


def auth_middleware(authorization: str = Header(None)):  # Changed x_auth_token to authorization
    try:
        if not authorization:
            raise HTTPException(status_code=401, detail="No auth token, access denied")

        # Check if the token starts with "Bearer " and extract the token
        if authorization.startswith("Bearer "):
            token = authorization[len("Bearer "):]
        else:
            raise HTTPException(status_code=401, detail="Token missing 'Bearer ' prefix")

        # Decode the token, with signature verification enabled
        verified_token = jwt.decode(token, secret_key, algorithms=["HS256"], options={"verify_exp": True})

        # Check if the token is valid (it's already checked with jwt.decode)
        if not verified_token:
            raise HTTPException(status_code=401, detail="Token verification failed, access denied")

        # Get the user id from the token
        uid = verified_token.get('id')
        if not uid:
            raise HTTPException(status_code=401, detail="User ID missing in token")
        
        return {'uid': uid, 'token': token}
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired, please login again")
    
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token is invalid, Authorization failed")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
  