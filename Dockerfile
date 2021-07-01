FROM golang:1.16.5-alpine
WORKDIR /
COPY . .
RUN go run .
FROM scratch AS bin
COPY --from=build /out/example /