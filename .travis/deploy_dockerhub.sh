docker login -u $DOCKER_USER -p $DOCKER_PASS
echo $TRAVIS_REPO_SLUG
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build -f Dockerfile -t imedznd/cicd-buzz:$TAG .
docker push imedznd/cicd-buzz:$TAG
