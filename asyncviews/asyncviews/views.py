import asyncio
import httpx
from django.http import JsonResponse

async def api(request):

    for n in range(1, 6):
        await asyncio.sleep(1)
        print(n)  
    
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")  
        print(r.status_code)  
        print(r.json())  
        
        return JsonResponse({"status_code": r.status_code, "response": r.json()})