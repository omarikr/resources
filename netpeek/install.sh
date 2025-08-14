#!/bin/bash

REPO_URL="https://raw.githubusercontent.com/omarikr/resources/main/netpeek"

echo "📥 Downloading Netpeek..."
curl -s -O "$REPO_URL/netpeek.py"
curl -s -O "$REPO_URL/requirements.txt"

echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

echo "⚙️ Making netpeek executable..."
chmod +x netpeek.py

echo "✅ Installation complete!"
echo "Run it with: ./netpeek.py"
