# ToyHouse uploader

I am using [PostyBirb+](https://github.com/mvdicarlo/postybirb-plus) for my uploading needs and they don't natively support Toyhouse. I didn't really have enough time to make a proper contribution to the repository, but at least I reverse engineered it enough to be useful enough to do uploads via custom provider.

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
