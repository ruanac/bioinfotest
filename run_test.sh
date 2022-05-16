docker build -t varsomics/bioinfotest .
docker container run --rm -it  -v $(pwd):/biotest  varsomics/bioinfotest

