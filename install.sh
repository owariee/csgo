#!/usr/bin/env bash
[ -z "${STEAM_ID3}" ] && STEAM_ID3=254174168
CSGO_USERDATA=~/.local/share/Steam/userdata/$STEAM_ID3/730
CFG_FOLDER=$CSGO_USERDATA/local/cfg
rm -rf $CSGO_USERDATA
mkdir -p $CFG_FOLDER
cp *.cfg $CFG_FOLDER 

