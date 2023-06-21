# TPC-DS Tool version 3.2

## Install software (Ubuntu)
```bash
# Ubuntu
sudo apt install g++-9 gcc-9 make
# Redhat
yum -y install g++-9 gcc-9 make
```

## Build tools. It needs gcc version 9
```bash
./bin/build-tool.sh
```

## Preparation data
scale:
1 - 1G
10 - 10G
100 - 100G
1000 - 1Tb

```bash
./bin/generate-data.sh <scale>
```

Example for 100 G
```bash
./bin/generate-data.sh 100 # 100 is scale
```

