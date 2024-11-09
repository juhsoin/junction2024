# Testing that container based workflow works

## Docker 

- Inspect compose.yaml and change the architecture arg based on the platform you are running on
- run ```docker compose build``` and ```docker compose up```


## running fastapi

- attach to the container with ```docker attach <container_tag>```

- go to /app/back

- Before running first time the api, run ````python3 add_mock_data.py``` to populate the database with mock data

- run ```fastapi dev --host 0.0.0.0``` to start the backend API

- navigate to localhost:8000/api in your browser and check do you receive the mock json response


## running vite dev

- attach to the container with ```docker attach <container_tag>```

- go to /app/front/vue-project and run ```npm run dev``` 

- navigate to localhost:5173 in your browser and check do you see the vue default page


## vscode specific stuff

- install remote development extension
- after spinning up the containers install necessary extensions inside the container environment (example in prep.sh)

## neovim specific stuff

- download neovim tar archive from https://github.com/neovim/neovim/releases/tag/v0.10.2
- extract and add `nvim-linux64/` folder to the root
- ensure that nvim mounts in `./compose.yaml` are uncommented
- start container and enjoy smooth neovim experience
