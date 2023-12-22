source ./stack_name.sh
CID=$(docker ps -qf "name=${STACK_NAME}_python-dev")
docker exec -it ${CID} /usr/bin/sh
