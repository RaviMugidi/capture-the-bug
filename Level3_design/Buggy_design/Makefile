# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/universal_shift_reg.v          # provide your design path

TOPLEVEL := universal_shift_reg        # design file
MODULE   := test_universal_shift_reg   # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
