#!/bin/bash

cd ../tools

make -f Makefile.suite CC=gcc-9 OS=LINUX

make -f Makefile.suite OS=LINUX