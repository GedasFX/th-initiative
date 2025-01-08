# ToyHouse uploader

I am using [PostyBirb+](https://github.com/mvdicarlo/postybirb-plus) for my uploading needs and they don't natively support Toyhouse. I didn't really have enough time to make a proper contribution to the repository, but at least I reverse engineered it enough to be useful enough to do uploads via custom provider.

## Update

It seems like the uploader no longer works due to cloudflare, and I will respect that and not update to bypass.

## Running

```yml
version: "3.8"

services:
  app:
    image: ghcr.io/gedasfx/th-initiative:main
    ports:
      - 8000:8000
    restart: unless-stopped
```

## Configuring PostyBirb

```
File URL:                 http://host:8000/upload    <- Change host to where its deployed
Title Field:              author
File Field:               file
Description Field:        caption
Description Parsing Type: Plain Text
Tag Field:                character_ids

Headers
Header 1:                 token | <TOKEN_SEE_BELOW>  <- key | value, do not copy the '<>'
```

###

### Obtaining Token

![image](https://github.com/GedasFX/th-initiative/assets/8672277/d49a6eda-3ba5-486d-83dc-b83f55ce5392)

## Usage in PostyBirb+

In general this is a hack, but it is what it is.

```
Title:       author
Description: caption
Tag Field:   character_ids
```

Author is required for posting, and at least one character id. I personally have set up some tag groups to name the characters.

## Troubleshooting

Logs can be found here:
![image](https://github.com/GedasFX/th-initiative/assets/8672277/4e3cc7ae-8fe4-40ff-9f1c-e4d418e9e39c)
![image](https://github.com/GedasFX/th-initiative/assets/8672277/423ed1f5-5b5a-42f5-a753-a15a3b34ed92)

### Known messasges

* **A valid source must be provided.** Unknown title. Remember, use title as the author.
* **You must select at least one character.** Self explanatory. Remember, use tags as character ids.
* **The caption may not be greater than 255 characters.** Self explanatory.
* **The image may not be greater than 4000 kilobytes.** Self explanatory.

