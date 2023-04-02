from django.shortcuts import render
import asyncio
import time
import httpx

from django.http import JsonResponse


# Create your views here.
async def http_call_async(url):
	print(f"async call to {url}...")
	async with httpx.AsyncClient() as client:
		await asyncio.sleep(1)
		r = await client.get(url)
		return r.json()

async def weather_async(request):
    tasks = []
    res = http_call_async("http://api.openweathermap.org/data/2.5/weather?q=" + request.GET['city'] + "&appid=fe4e867dcd8afc52b9c4bff66707242e")
    tasks.append(res)
    responses = await asyncio.gather(*tasks)
    result = {"responses": responses}
    return JsonResponse(result, safe=False)

def tampilan(request):
    response={}
    return render(request,'weather/weather_search.html',response)