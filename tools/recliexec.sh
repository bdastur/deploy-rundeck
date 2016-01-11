#!/bin/bash

# Execute a CLI on remote hosts.

RUNDECK_TOOLS_HOME="/data/rundeck/tools"
RCLI="${RUNDECK_TOOLS_HOME}/relic/relic/remote_run.py"

echo $RD_OPTION_HOSTS
echo $RD_OPTION_USERNAME
echo $RD_OPTION_COMMAND

${RCLI} -r $RD_OPTION_HOSTS \
    --username $RD_OPTION_USERNAME \
    --password $RD_OPTION_PASSWORD \
    --adhoc $RD_OPTION_COMMAND

