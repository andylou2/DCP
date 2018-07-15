#!/bin/bash

DATE=`date +%m_%d_%Y`
touch "$DATE".py

sublime "$DATE".py
