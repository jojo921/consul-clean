# Introduction

A simple consul tools which will clean up all services with critical status
in the DC where the consul agent listening on the address pointed by ```the host param and port param``` lies in

## Install
```
curl https://raw.githubusercontent.com/jojo921/consul-cleanup/master/requirements.txt \
    -o requirements.txt &&\
    pip install -r requirements.txt &&\
    rm requirements.txt &&\
    curl https://raw.githubusercontent.com/jojo921/consul-cleanup/master/consul-cleanup.py -o consul-cleanup

```
## Usage
```
python consul-cleanup -h
```
