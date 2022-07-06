import datetime

config = {
    "Cookie": "",  # dev tools > request headers
    "_csrf": "",  # dev tools > payload
    "authorizedID": "",  # registration number
    "x": datetime.datetime.now(datetime.timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    ),
}
