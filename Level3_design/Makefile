# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/Universal_shift_reg.v              # provide your design path

TOPLEVEL :=           Universal_shift_reg.v
MODULE   :=     tb_universal_shift_reg.py

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__
