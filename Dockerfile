FROM ghcr.io/qubitdimensions/fizilion:dev
RUN mkdir /Fizilion && chmod 777 /Fizilion && git clone https://github.com/arshsisodiya/ProjectFizilion -b demon /Fizilion
WORKDIR /Fizilion
CMD ["python3","-m","bot"]
