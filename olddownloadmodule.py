import requests
import time
import uuid


def download_file(url):
    #filename = str(uuid.uuid4())
    with requests.get(url, stream=True) as req:
        with open("ddmRequests", 'wb') as f:
            for chunk in req.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
        print(req.headers['content-type'])
        print(req.status_code)


if __name__ == "__main__":
    site = "https://github.com/XDream8/DDM/releases/download/v0.210Alpha/ddm_LinuxPreRelease_v0.210AlphaVersion"
    start_time = time.time()
    #duration = time.time() - start_time
    #loop = asyncio.get_event_loop()
    # loop.run_until_complete(download_file(url))
    download_file(site)
    duration = time.time() - start_time
    print(duration)
