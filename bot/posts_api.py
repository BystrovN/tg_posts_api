import logging
from typing import Literal, Optional

import httpx

from .config import API_URL

logger = logging.getLogger(__name__)


async def _api_request(
    url: str,
    method: Literal['GET', 'POST', 'PUT', 'DELETE', 'PATCH'] = 'GET',
    data: Optional[dict] = None,
    params: Optional[dict] = None,
) -> httpx.Response:
    """Отправка API запроса."""
    async with httpx.AsyncClient() as client:
        response = await client.request(method=method, url=url, json=data, params=params)
        logger.info(f'{method} request to {url}: status - {response.status_code}, body - {response.text[:100]}')
        response.raise_for_status()
        return response


async def fetch_posts() -> list:
    """Получение списка постов."""
    response = await _api_request(API_URL)
    return response.json()['items']


async def fetch_post_detail(post_id: int):
    """Получение поста по id."""
    response = await _api_request(f'{API_URL}{post_id}/')
    return response.json()
