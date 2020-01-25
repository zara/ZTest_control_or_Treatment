FROM continuumio/miniconda:latest
WORKDIR /home/docker_conda_template

COPY environment.yml ./
COPY api.py ./
COPY boot.sh ./

RUN chmod +x boot.sh

RUN conda env create -f environment.yml -n b2

RUN echo "source activate b2" > ~/.bashrc

ENV PATH /opt/conda/envs/b2/bin:$PATH

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]