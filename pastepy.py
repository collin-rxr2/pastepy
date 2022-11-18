import requests

def request_paste(data):
    return requests.post("https://pastebin.com/api/api_post.php", data=data).text

def new(key, title, content, language="none"):
    if language=="none":
        data = {
            "api_dev_key": key,
            "api_paste_private": "0",
            "api_paste_name": title,
            "api_paste_code": content,
            "api_option": "paste",
        }
    else:
        data = {
            "api_dev_key": key,
            "api_paste_private": "0",
            "api_paste_name": title,
            "api_paste_code": content,
            "api_option": "paste",
            "api_paste_format": language
        }
    return request_paste(data)
