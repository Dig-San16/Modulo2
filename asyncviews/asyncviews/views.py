import asyncio
import httpx
from django.http import HttpResponse

async def async_view(request):
    contador = []
        for i in range(1, 6):
            contador.append(f"Segundo {i}")
            await asyncio.sleep(1)  # Pausa de 1 segundo
    
        return JsonResponse({"contador": contador})
