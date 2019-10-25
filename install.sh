#!/bin/bash -e

echo "[Easy] Commencing installation..."
echo ""
cat title.txt
echo ""

#Check system 
if [[ "$(uname)" == 'Linux' ]]; then
	if [ $(which apt) ]; then
		echo "[Easy] Installing system requirements..."
		sudo apt install python3 espeak
	fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
	if [ ! $(which brew) ]; then
		echo "[Easy] Installing brew..."
		/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	fi
	echo "[Easy] Installing Python3..."
	brew install python3
fi

if [ $(ls -a | grep .happy) == ".happy" ]; then
	sudo chmod 775 easyonset.py
	echo "[Easy] Generating symlink..."
	sudo ln -sf $HOME/Easyonset/easyonset.py /usr/local/bin/easy
	mv ../Easyonset $HOME
	echo "[Easy] Installation complete. Speak easy."
else
	echo "[Easy] Please navigate to the Easyonset folder and restart installation.."
fi
