import asyncio
import aiohttp
import time
import uuid
import async_timeout


async def download_file(url):
    async with aiohttp.ClientSession() as session:
        filename = str(uuid.uuid4())
        async with async_timeout.timeout(120):
            async with session.get(url) as response:
                #        with open("ddmLinuxPreRelease", 'wb') as fd:
                #            async for data in response.content.iter_chunked(1024 * 8):
                #                fd.write(data)

                assert response.status == 200
                print(response.headers['Content-Length'])
                print(response.status)


if __name__ == "__main__":
    url = "https://github.com/XDream8/DDM/releases/download/v0.210Alpha/ddm_LinuxPreRelease_v0.210AlphaVersion"
    start_time = time.time()
    duration = time.time() - start_time
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_file(url))
    # download_file(url)
    duration = time.time() - start_time
    print(duration)
