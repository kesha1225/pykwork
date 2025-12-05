import logging
from types import TracebackType
from typing import Any, Self

import aiohttp
from kwork.exceptions import KworkException

logger = logging.getLogger(__name__)

AUTH_HEADER = "Basic bW9iaWxlX2FwaTpxRnZmUmw3dw=="
API_HOST = "https://api.kwork.ru/{}"


class KworkAPI:
    def __init__(
        self,
        login: str,
        password: str,
        proxy: str | None = None,
        phone_last: str | None = None,
    ) -> None:
        self._session: aiohttp.ClientSession | None = None
        self._connector = self._create_connector(proxy)
        self._login = login
        self._password = password
        self._phone_last = phone_last
        self._token: str | None = None

    @staticmethod
    def _create_connector(proxy: str | None) -> aiohttp.BaseConnector | None:
        if proxy is None:
            return None

        try:
            from aiohttp_socks import ProxyConnector
        except ImportError as err:
            msg = "Install aiohttp_socks for proxy support: pip install aiohttp_socks"
            raise ImportError(msg) from err

        return ProxyConnector.from_url(proxy)

    @property
    def session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(connector=self._connector)
        return self._session

    async def close(self) -> None:
        if self._session is not None and not self._session.closed:
            await self._session.close()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def get_token(self) -> str:
        if self._token is not None:
            return self._token

        body: dict[str, str] = {
            "login": self._login,
            "password": self._password,
        }
        if self._phone_last is not None:
            body["phone_last"] = self._phone_last

        response = await self.request_with_body("signIn", body=body)
        token: str = response["response"]["token"]
        self._token = token
        return token

    async def request(
        self,
        method: str,
        endpoint: str,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        filtered = {k: v for k, v in params.items() if v is not None}

        if use_token:
            filtered["token"] = await self.get_token()

        logger.debug("Request %s /%s params=%s", method.upper(), endpoint, filtered)

        async with self.session.request(
            method=method,
            url=API_HOST.format(endpoint),
            headers={"Authorization": AUTH_HEADER},
            params=filtered,
        ) as resp:
            return await self._handle_response(resp, endpoint)

    async def _handle_response(
        self,
        resp: aiohttp.ClientResponse,
        endpoint: str,
    ) -> dict[str, Any]:
        if resp.content_type != "application/json":
            error_text = await resp.text()
            raise KworkException(f"Non-JSON response from /{endpoint}: {error_text}")

        data: dict[str, Any] = await resp.json()

        if not data.get("success"):
            raise KworkException(data.get("error", "Unknown API error"))

        logger.debug("Response /%s: %s", endpoint, data)
        return data

    async def request_with_body(
        self,
        endpoint: str,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        filtered_params = {k: v for k, v in params.items() if v is not None}

        if use_token:
            filtered_params["token"] = await self.get_token()

        logger.debug(
            "Request POST /%s params=%s body=%s",
            endpoint,
            filtered_params,
            body,
        )

        async with self.session.post(
            url=API_HOST.format(endpoint),
            headers={"Authorization": AUTH_HEADER},
            params=filtered_params,
            data=body,
        ) as resp:
            return await self._handle_response(resp, endpoint)
