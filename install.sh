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

echo "Generating symlink..."
sudo ln -sf $(pwd)/easyonset.py /usr/local/bin/easy
sudo chmod 775 easyonset.py

echo "Installation complete. Speak easy."
