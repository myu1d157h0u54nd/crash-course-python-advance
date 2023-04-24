# Python

sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip

## python jupyter

pip install notebook rise
jupyter --version

jupyter notebook

# Docker

sudo apt update
sudo apt upgrade
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
apt-cache policy docker-ce

sudo systemctl status docker
sudo usermod -aG docker ${USER}
su - ${USER}
groups

# Pyenv
sudo apt update
sudo apt upgrade

sudo apt install git curl -y 

sudo apt-get install python-tk python3-tk tk-dev build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev libncurses-dev

curl https://pyenv.run | bash

export PATH="$HOME/.pyenv/bin:$PATH" && eval "$(pyenv init --path)" && echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

exec $SHELL

pyenv --version


## How to Uninstall Pyenv on Ubuntu?
To uninstall the pyenv on Ubuntu, we will remove the folder of the pyenv by using the rm command:

$ rm -fr ~/.pyenv