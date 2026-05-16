import httpx


class DocHandler4AIClient:

    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout: int = 300
    ):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    async def post(
        self,
        endpoint: str,
        json: dict
    ):

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        async with httpx.AsyncClient(
            timeout=self.timeout
        ) as client:

            response = await client.post(
                f"{self.base_url}{endpoint}",
                json=json,
                headers=headers
            )

            response.raise_for_status()

            return response.json()