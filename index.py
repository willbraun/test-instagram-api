import requests
import json

token = 'IGQVJXaGlud09iM0JWUFA4RTl3SkltOHFtNFE4Y1BDQkpSdGpLYXNZAaXpnZAmdXNDlkdjFqRmtZANVZAuclRQeE5kWHMxZA2kxQkpfRTA2Wkp5WENXakxpV3IxVWs2dmhoTFh6TXloQlN3'

response_all = requests.get(f'https://graph.instagram.com/me?fields=media&access_token={token}')

decoded_all = json.loads(response_all.text)
id_objects = decoded_all['media']['data']

def get_caption(id_object):
    this_id = id_object['id']
    url = f'https://graph.instagram.com/{this_id}?fields=caption&access_token={token}'
    response_media = requests.get(url)
    decoded_media = json.loads(response_media.text)
    caption = decoded_media['caption']
    return caption

captions = list(map(get_caption, id_objects))

print(captions)