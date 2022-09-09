FROM golang:1.9
ENV GOLANG_VERSION 1.9
WORKDIR $GOPATH/src/dockerfile/app
COPY . .
RUN apt update && apt install ca-certificates libgnutls30 -y
RUN go get -d -v ./...
RUN go install -v ./...
CMD ["app"]