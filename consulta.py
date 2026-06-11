import requests
from requests.auth import HTTPDigestAuth

r = requests.get(
    "http://192.168.0.212/ISAPI/System/deviceInfo",
    auth=HTTPDigestAuth("admin", "Admin@23646"),
    timeout=5,
)
print(r.text if r.status_code == 200 else f"Error: {r.status_code}\n{r.text}")
