from .client import DocHandler4AIClient
from .pdf import PDFAPI


class DocHandler4AI:
    
    def __init__(self,base_url:str,api_key: str,):
        client = DocHandler4AIClient(base_url,api_key)
        self.pdf = PDFAPI(client) 
    