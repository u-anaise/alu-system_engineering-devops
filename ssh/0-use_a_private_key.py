#!/usr/bin/env bash
# Connects to the server as the user ubuntu using the private key ~/.ssh/school
ssh -o IdentityFile=~/.ssh/school ubuntu@18.175.239.114
