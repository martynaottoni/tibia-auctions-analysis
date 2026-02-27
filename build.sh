#!/bin/bash
set -o errexit

# Install Python 3.11
apt-get update
apt-get install -y python3.11 python3.11-venv python3.11-dev

# Use Python 3.11
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
