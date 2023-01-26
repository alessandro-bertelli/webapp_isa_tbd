FROM continuumio/anaconda3

LABEL maintainer "Alessandro Bertelli <alessandro.bertelli@edu.unife.it>"

WORKDIR /app

COPY environment.yml ./

RUN conda env create -f environment.yml

# Attivo l'ambiente virtuale
SHELL ["conda", "run", "-n", "proj_env", "/bin/bash", "-c"]

# Copio i file sorgente all'interno del container
COPY src/ ./src/
COPY tests/ ./tests/
COPY test_start.sh .

RUN chmod +x test_start.sh
RUN chmod +x src/start.sh

EXPOSE 5000

ENTRYPOINT ["./src/start.sh"]
