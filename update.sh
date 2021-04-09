#!/bin/bash
echo "[!] ADDING TO GIT REPO"
git add .
echo "[!] STATUS:"
git status
echo "[!] COMMIT:"
read msg
git commit -m "${msg}"
echo "[!] PUSHING TO REMOTE"
git push
