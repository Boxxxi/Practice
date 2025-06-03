REGISTRY="661900564209.dkr.ecr.ap-south-1.amazonaws.com"

if [ "$1" == 'prod' ]
then
    REPOSITORY="dc-custom-ner-model"
else
    REPOSITORY="dc-custom-ner-model-$1"
fi

BUILD_IDENTIFIER="$2"

# Build image with commit id as tag
docker build \
    --tag custom-ner:$BUILD_IDENTIFIER \
    --platform linux/amd64 \
    -f "Dockerfile" .

IMAGE_ID=$(docker images --filter=reference=custom-ner:$BUILD_IDENTIFIER --format "{{.ID}}")

# Get AWS ECR login
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin $REGISTRY

# Tag image with commit id
docker tag $IMAGE_ID $REGISTRY/$REPOSITORY:$BUILD_IDENTIFIER

# Push image to ECR
docker push $REGISTRY/$REPOSITORY:$BUILD_IDENTIFIER

# Log 
echo "\n\n\tImage ID: $BUILD_IDENTIFIER"