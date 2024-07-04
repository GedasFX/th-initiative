import re
import requests
import uvicorn
from bs4 import BeautifulSoup 
from typing import Annotated
from fastapi import FastAPI, File, Form, HTTPException, Header, UploadFile

def get_csrf_tokens(refresh_token: str):
    response = requests.get('https://toyhou.se/~images/upload', cookies = { "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d": refresh_token })
    
    if response.url == 'https://toyhou.se/~account/login':
        raise HTTPException(status_code=401, detail="Refresh token")
    
    csrf_token_body = BeautifulSoup(response.text, features="html.parser").select("head > meta[name='csrf-token']")[0]['content']
    csrf_token_header = re.search(r'XSRF-TOKEN=([\w%]+);', response.headers['set-cookie']).group(1)
    laravel_session = re.search(r'laravel_session=([\w%]+);', response.headers['set-cookie']).group(1)

    return [csrf_token_body, csrf_token_header, laravel_session]

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile, token: Annotated[str, Header()], author: Annotated[str, Form()], caption: Annotated[str, Form()], character_ids: Annotated[str, File()]):
    tokens = get_csrf_tokens(token)

    form_data = [
        ('_token', (None, tokens[0])),
        ('image', (file.filename, file.file, file.content_type)),
        ('thumbnail_options', (None, 'onsite')), # 
        ('thumbnail_custom', (None, 'offsite')), # 
        ('image_zoom', (None, '')), # 
        ('image_x', (None, '')), # 
        ('image_y', (None, '')), # 
        ('image_data', (None, '')), # 
        ('thumbnail', ('', '', 'application/octet-stream')), # 
        ('caption', (None, caption)),
        ('authorized_privacy', (None, '0')), #
        ('public_privacy', (None, '0')), #
        ('watermark_id', (None, '1')), #
        ('is_sexual', (None, '0')), #
        ('warning', (None, '')), #
        ('artist[]', (None, 'onsite')),
        ('artist_username[]', (None, author)),
        ('artist_url[]', (None, '')),
        ('artist_name[]', (None, '')),
        ('artist_credit[]', (None, '')),
        ('artist[]', (None, 'onsite')),
        ('artist_username[]', (None, '')),
        ('artist_url[]', (None, '')),
        ('artist_name[]', (None, '')),
        ('artist_credit[]', (None, '')),
    ]

    for character_id in character_ids.split(','):
        form_data.append(('character_ids[]', (None, character_id)))
    form_data.append(('character_ids[]', (None, '')))

    result = requests.post('https://toyhou.se/~images/upload', cookies = { "laravel_session": tokens[2], 'XSRF-TOKEN': tokens[1] }, files = form_data )
    
    err = BeautifulSoup(result.text, features="html.parser").select(".alert-danger")
    if len(err) > 0:
        raise HTTPException(status_code=400, detail=err[0].text.strip())
    
    return result.url


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)