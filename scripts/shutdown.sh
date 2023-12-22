source ./stack_name.sh
echo "Preparing to stop ${STACK_NAME}..."

docker stack rm ${STACK_NAME}

echo "Shutting down ${STACK_NAME}..."
while [ "$(docker ps | grep ${STACK_NAME})" ]; do
  printf "."  && sleep 2
done;

echo "Shut down of ${STACK_NAME} complete."
