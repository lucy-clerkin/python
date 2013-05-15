PYTHON=python
# List of all .dat files in inputs/
INS=$(wildcard inputs/*.dat)
# Use list of all .dat files in inputs/ to create list of
# corresponding .out file names in outputs.
OUTS=$(patsubst inputs%, outputs%, $(patsubst %.dat, %.out, $(INS)))

all: outputs

outputs: $(OUTS)

clean-outputs:
	@rm -f outputs/*.out

clean : clean-outputs
	@rm -f *~ *.pyc
