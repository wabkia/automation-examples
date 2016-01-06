#!/bin/bash 

# log output and display status in console
exec >  >(tee -a "$USER"-install.log)
exec 2> >(tee -a "$USER"-error.log >&2)

# Set some global variables
VWX_INSTALLER_PATH="${0%/*}"
# echo $VWX_INSTALLER_PATH
VWX_INSTALLER="Install\ Vectorworks2016.app/Contents/MacOs/installbuilder.sh"
COMP_NAME="--CompName \"Corp Name\""
MODE="--mode unattended"
SERIAL="--Serial long-serial-number-thing"
FULL_NAME="--UserName \"$(eval 'osascript -e "long user name of (system info)"')\""
# echo $FULL_NAME
USER_NAME="$(eval whoami)"
# echo $USER_NAME

# gather information from tech
echo -n "Is this a Spotlight or Renderworks install?"
read USER_MODULES

# move into directory script was run from
cd "${0%/*}"

# run install command
eval $VWX_INSTALLER $MODE $SERIAL $COMP_NAME $FULL_NAME

# copy licensing server config
if [ -d /Users/$USER_NAME/Library/Application\ Support/Vectorworks/2016/Settings/SeriesG ]
then
    case "$USER_MODULES" in
        spotlight|Spotlight|s)
            echo "Copying Spotlight Config"
            eval "cp 'LoginDialog-spotlight.xml/' /Users/$USER_NAME/Library/Application\ Support/Vectorworks/2016/Settings/SeriesG/LoginDialog.xml"
            echo "Site Protection Server configuration copied";;
        renderworks|Renderworks|r)
            echo "Copying Renderworks Config"
            eval "cp 'LoginDialog-renderworks.xml/' /Users/$USER_NAME/Library/Application\ Support/Vectorworks/2016/Settings/SeriesG/LoginDialog.xml"
            echo "Site Protection Server configuration copied";;
        *)
            echo "Did you select renderworks or spotlight? - Copy config manually to 'Users/$USER_NAME/Library/Application\ Support/Vectorworks/2016/Settings/SeriesG/'"
            read -rsp $'Press Any key to continue...\n' -n1 key
else
    echo "SeriesG folder not present. Attempt re-install"
    exit    
fi
