# Fingrid Junction 2024 Challenge by team 70s Pöhinä
A solution to centralize the feature request data and encourage collaboration between different parties

Content of this README:
- Short motivation for the project
- Short introduction to technical choices
- How to run the project locally


## Motivation
Fingrid Datahub is a centralized data exchange system for the electricity retail market, storing information on around 3.8 million electricity points of use ([source](https://www.fingrid.fi/en/electricity-market/datahub/)). Managing all the feature requests and changes can get complicated: each new feature needs to go through many different working committee meetings and the processes can be long. The data from the original feature request need and more recent updates are scattered to many different files ranging from excel-files to meeting transcript -pdfs. 

Our project aims to solve this problem, by centralizing data, empowering collaboration, and tailoring user experience. Our platform collects all the information relating to feature requests in one place, where each user can personalize their own stream to follow the updates that are the most important for them. On the platform, users can give feedback to new and ongoing initiatives by liking and commenting, allowing faster feedback loops and better interaction.


## Short introduction of technical choices
- The backend is created using Python due to its common use and versatile libraries.
- FastAPI was chosen for its ease of use, quick setting-up, and good standardization.
- For the database, SQLite was used, as it could be setting it up needs only an accessible file.
- Vue was used for the front end, as it offers a good collection of components.
- NOTE: The best user experience is on the Chrome-browser.


## How to run Project locally
### Docker 
- Inspect compose.yaml and change the architecture arg based on the platform you are running on
- run `docker compose build` and `docker compose up`

### Running Fastapi
- attach to the container with `docker attach <container_tag>`
- go to /app/back
- Before running first time the api, run ``python3 add_mock_data.py` to populate the database with mock data
- run `fastapi dev --host 0.0.0.0` to start the backend API
- navigate to localhost:8000/api in your browser and check do you receive the mock json response

### Running Vite dev
- attach to the container with `docker attach <container_tag>`
- go to /app/front`
- run `npm ci` to build packages (only needed first time)
- run `npm run dev` to launch the service
- navigate to localhost:5173 in your browser and check do you see the vue default page

### Vscode specific stuff
- install remote development extension
- after spinning up the containers install necessary extensions inside the container environment (example in prep.sh)

### Neovim specific stuff
- download neovim tar archive from https://github.com/neovim/neovim/releases/tag/v0.10.2
- extract and add `nvim-linux64/` folder to the root
- ensure that nvim mounts in `./compose.yaml` are uncommented
- start the container and enjoy a smooth neovim experience