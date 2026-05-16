from .client import DocHandler4AIClient
from typing import Literal

class PDFAPI:

    def __init__(self, client: DocHandler4AIClient):
        self.client = client

    async def process(
        self,
        pdf_url: str,
        response_output: Literal['chunks','markdown'] = "chunks",
        max_tokens: int = 500,
        image_to_text_model: str | None = None,
        formula_to_latex_model: str | None = None,
        id: str | None = None
    )->str | list[str]:

        payload = {
            "id": id,
            "pdf_url": pdf_url,
            "max_tokens": max_tokens,
            "image_to_text_model": image_to_text_model,
            "formula_to_latex_model": formula_to_latex_model
        }
        
        return await self.client.post(f"/pdf/{response_output}",payload)
    

