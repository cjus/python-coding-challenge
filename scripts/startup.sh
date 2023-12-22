source ./stack_name.sh
docker stack deploy --compose-file stack-compose.yml --with-registry-auth ${STACK_NAME}

echo "Use ./shell.sh to enter the development container shell"
