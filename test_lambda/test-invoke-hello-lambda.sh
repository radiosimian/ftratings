#!/bin/bash

# Invoke hello-py lambda
/usr/local/bin/aws lambda invoke \
--invocation-type RequestResponse \
--function-name "hello-py" \
--region eu-west-1 \
--log-type Tail \
--payload '{"first_name":"Groggy", "last_name":"McTired"}' \
--profile admin-simon \
outputfile.txt

# Voila!!
cat outputfile.txt
