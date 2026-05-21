#!/bin/bash
cd /home/ubu/app-code
# Скачиваем код ветки lab1
git fetch origin
git reset --hard origin/lab1
# Перезапускаем сайт
sudo systemctl restart catty-app.service
