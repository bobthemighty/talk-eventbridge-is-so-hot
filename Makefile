MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_DIR := $(patsubst %/,%,$(dir $(MKFILE_PATH)))
DIAGRAMS_DIR = $(ROOT_DIR)/diagrams

all: render_diagrams serve

render_diagrams:
	$(foreach file, $(wildcard $(DIAGRAMS_DIR)/*.py), cd $(DIAGRAMS_DIR) && python $(file);)

serve:
	python -m http.server
