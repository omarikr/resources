#!/bin/bash

REPO_URL="https://raw.githubusercontent.com/omarikr/resources/main/netpeek"
INSTALL_PATH="/usr/local/bin/netpeek"

echo "📥 Downloading Netpeek..."
curl -s -L "$REPO_URL/netpeek.py" -o netpeek.py
curl -s -L "$REPO_URL/requirements.txt" -o requirements.txt

echo "📦 Installing dependencies..."
pip3 install --user -r requirements.txt

echo "⚙️ Installing Netpeek globally..."
chmod +x netpeek.py
sudo mv netpeek.py $INSTALL_PATH

echo "✅ Installation complete!"
echo "You can now run 'netpeek' from anywhere."
