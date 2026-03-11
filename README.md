# StorySpark Legal

Microsite estático da StorySpark para página institucional leve e documentos legais por aplicativo.

## Estrutura

- `index.html`: home institucional com links para os apps
- `legal/<app>/privacy/`: política de privacidade por app
- `legal/<app>/data-deletion/`: instruções de exclusão de dados por app
- `styles.css`: estilo compartilhado
- `Dockerfile` e `docker-compose.yml`: publicação estática com Nginx atrás do Traefik

## Apps atuais

- Fresta
- Senda
- OmniWell

## Deploy manual na VPS

```bash
cd /root/storyspark-legal
git pull
docker compose up -d --build
```

## Rebuild local

```bash
docker compose up -d --build
```

## URLs públicas

- `https://storyspark.com.br/`
- `https://storyspark.com.br/legal/fresta/privacy/`
- `https://storyspark.com.br/legal/fresta/data-deletion/`
- `https://storyspark.com.br/legal/senda/privacy/`
- `https://storyspark.com.br/legal/senda/data-deletion/`
- `https://storyspark.com.br/legal/omniwell/privacy/`
- `https://storyspark.com.br/legal/omniwell/data-deletion/`
