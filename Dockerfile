FROM continuumio/miniconda:latest

LABEL maintainer "Alessandro Bertelli <alessandro.bertelli@edu.unife.it>"

RUN apt-get --allow-releaseinfo-change update

RUN mkdir /app

WORKDIR /app

COPY environment.yml ./
COPY test_start.sh ./

ADD tests ./tests
ADD src ./src

RUN chmod +x test_start.sh
RUN chmod +x src/start.sh

RUN conda env create -f environment.yml

RUN echo "source activate proj_env"; ~/.bashrc
ENV PATH /opt/conda/envs/proj_env/bin:$PATH

EXPOSE 5000

ENTRYPOINT ["./src/start.sh"]
