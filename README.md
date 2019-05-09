# introduction

A simple consul tools which will clean up all services with critical status
in the DC where the consul agent listening on the address pointed by ```the host param and port param``` lies in

## install
```
curl https://raw.githubusercontent.com/jojo921/consul-clean/master/requirements.txt \
    -o requirements.txt &&\
    pip install -r requirements.txt &&\
    rm requirements.txt &&\
    curl https://raw.githubusercontent.com/jojo921/consul-clean/master/consul-clean.py -o consul-clean

```
## Usage
```
python consul-clean -h
```
