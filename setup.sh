#!/bin/bash

###########################################################
# Execute the script to setup Rundeck environment.
# The script does not install rundeck. But instead setups up
# Other tools and repositories after that.
###########################################################
RUNDECK_TOOLS_HOME="/data/rundeck/tools"


git clone https://github.com/bdastur/relic.git "$RUNDECK_TOOLS_HOME/relic"

