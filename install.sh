#!/bin/bash
echo "Making directories"
mkdir -p ~/.config/i3
mkdir -p ~/.config/i3status

echo "Installing i3 files"
cp i3/config ~/.config/i3/config
cp i3status/config ~/.config/i3status/config

echo "Installing bashrc"
cp .bashrc ~/.bashrc

echo "Installing i3lock files"
# sudo yaourt -S i3lock-color-git
sudo cp i3lock-fancy/lock /usr/local/bin
sudo cp i3lock-fancy/lock.png /usr/local/bin
