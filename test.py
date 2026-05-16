from docHandler4AISDK import DocHandler4AI
import asyncio 

async def main():
    
    sdk = DocHandler4AI('http://localhost:8000','123456789')
    
    result = await sdk.pdf.process(
        pdf_url="/home/simo/projects/simo-project/langchain-tuto/demo/docling/fic00001.pdf",
        
    )
    print(result)
     

asyncio.run(main())