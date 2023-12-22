# Syntax: ./build.sh
# Use --no-cache=true  when necessary
VERSION_TAG=$(<VERSION)
#docker buildx build --platform=linux/amd64,linux/arm64 --push --no-cache -t python-dev:$VERSION_TAG .
docker build -t python-dev:$VERSION_TAG .
