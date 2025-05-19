sudo apt-get update
sudo apt install -y python3 python3-pip podman
sudo snap install task --classic
python3 -m venv venv
source venv/bin/activate
python3 -m pip install poetry
poetry build
poetry install
