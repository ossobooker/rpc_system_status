# RPC Known Problems

## MongoDB

```
docker run --name mongodb -v "$(pwd)"/dbstore:/data/db -p 27017:27017 --rm mongo:5.0.4
```

## Setup env

```
python3 -m venv rpc_known_problems_env
```

## Run

```
uvicorn main:app --reload
```
