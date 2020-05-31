## Bot for telegramm

@sasc_bot

## Dev Env 

```shell script
$ docker-compose up -d
```

## Dump unicode FIX

Чтобы не ругалась алхимия:
```shell script
$ sed -i 's/utf8mb4_0900_ai_ci/utf8mb4_unicode_ci/g' ./docker-entrypoint-initdb.d/bot_db.sql
```

1217627259:AAHLhp3fS6FV5v4YJs2wy1-mNMJTmGcQdc0
