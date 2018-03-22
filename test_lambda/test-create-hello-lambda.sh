#!/bin/bash

# Create Lambda function and upload prepared zip file
echo "Creating Lambda Function: Hello.py"

/usr/local/bin/aws lambda create-function \
--region eu-west-1 \
--function-name hello-py \
--zip-file fileb://hello.zip \
--role arn:aws:iam::848695267852:role/ftratings-lambda-role \
--handler hello.hello-py \
--runtime python2.7 \
--timeout 15 \
--memory-size 512