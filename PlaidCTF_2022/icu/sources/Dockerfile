FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y cargo
RUN apt-get install -y pkg-config clang libleptonica-dev libtesseract-dev tesseract-ocr-eng

COPY . /icu
WORKDIR /icu
RUN cargo build --release

CMD cargo run --release
