from fastapi import APIRouter, FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import requests

from middleware.auth_middleware import auth_middleware

router = APIRouter()
BASE_URL = "https://api.coingecko.com/api/v3"

@router.get("/coins")
def list_coins(page_num: int = 1, per_page: int = 10, auth_details = Depends(auth_middleware)):
    """Lists all available coins."""
    url = f"{BASE_URL}/coins/markets"
    params = {"vs_currency": "cad", "page": page_num, "per_page": per_page}
    response = requests.get(url, params=params)
    return response.json()


@router.get("/categories")
def list_categories(auth_details = Depends(auth_middleware)):
    """Lists all cryptocurrency categories."""
    url = f"{BASE_URL}/coins/categories"
    response = requests.get(url)
    return response.json()


@router.get("/coins/{coin_id}")
def get_coin_details(coin_id: str, auth_details = Depends(auth_middleware)):
    """Gets details of a specific coin in CAD."""
    url = f"{BASE_URL}/coins/{coin_id}"
    response = requests.get(url, params={"localization": "false"})
    return response.json()
