import asyncio
import aiohttp
import time

url = "https://httpbin.org/delay/2" #gives response after the delay

async def fetch_url(session , url):
    async with session.get(url) as response:
        print(f"Fetch {url} with status {response.status} ")


async def main():
    urls = [url]*3  # 3* 2 sec delay means 6 sec total delay
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print(f"Operation took {end-start:.2f} seconds")

# Output
# Fetch https://httpbin.org/delay/2 with status 200 
# Fetch https://httpbin.org/delay/2 with status 200 
# Fetch https://httpbin.org/delay/2 with status 200 
# Operation took 3.39 seconds




















# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
#     "Accept-Encoding": "gzip, deflate, br, zstd", 
#     "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6", 
#     "Host": "httpbin.org", 
#     "Priority": "u=0, i", 
#     "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Google Chrome\";v=\"150\"", 
#     "Sec-Ch-Ua-Mobile": "?0", 
#     "Sec-Ch-Ua-Platform": "\"Windows\"", 
#     "Sec-Fetch-Dest": "document", 
#     "Sec-Fetch-Mode": "navigate", 
#     "Sec-Fetch-Site": "none", 
#     "Sec-Fetch-User": "?1", 
#     "Upgrade-Insecure-Requests": "1", 
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36", 
#     "X-Amzn-Trace-Id": "Root=1-6a55994d-19919b025963731d749cb6c7"
#   }, 
#   "origin": "223.184.190.226", 
#   "url": "https://httpbin.org/delay/1"