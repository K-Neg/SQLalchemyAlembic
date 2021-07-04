# FastApi with Postgres and compose


## Run:
docker build -t api .
docker compose up

## Locahost ports (defined at compose file):
> localhost:5100/docs - API
> localhost:5050 - PgAdmin

## Database url be like:
postgresql://{user}:{password}@{postgresserver}:{port}/{db_name}