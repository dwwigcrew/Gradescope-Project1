#!/usr/bin/env bash

apt-get -y install gcc

apt-get install -y python python-pip python-dev

pip install -r /autograder/source/requirements.txt
