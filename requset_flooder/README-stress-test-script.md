### Description:
This Python script performs continuous HTTP GET requests to a specified URL with precise control over the number of requests per second. The script is designed to be run indefinitely, with the ability to stop execution manually. Additionally, it dynamically adjusts for latency to ensure the desired request rate is maintained.

### Requirements:
```aiohttp library```
to install - ```pip install aiohttp```

### Usage:
1.Set environment variables
```REQUEST_URL```: The URL to which the requests will be sent. Default is ```https://example.com```.
```REQUESTS_PER_SECOND```: The number of requests to send per second. Default is ```10```

2.Run the script
```REQUST_URL="http://example.com" REQUSTS_PER_SECOND=10 python3 <file_name>```

### Stop the script:
Manually stop the script using Ctrl+C. The script will log a message indicating it has been interrupted.

### Output:
```2024-08-15 12:34:56.789 [INFO] Request 1: Status Code: 200, Latency: 0.0321 seconds```
