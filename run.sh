PORT=${1-:6543}
docker build -t pyramid_openapi3_headers_testcase .
docker run --name pyramid_openapi3_headers_testcase -d -p $PORT:6543 pyramid_openapi3_headers_testcase
sleep 5
curl localhost:$PORT/hello
docker logs pyramid_openapi3_headers_testcase
docker rm -f pyramid_openapi3_headers_testcase
