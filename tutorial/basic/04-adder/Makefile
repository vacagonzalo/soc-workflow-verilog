SOURCES=adder_tb.v adder.v
.PHONY: all clean adder.vcd adder_tb.vvp

all: adder.vcd

adder.vcd: adder_tb.vvp
	vvp $<

adder_tb.vvp: $(SOURCES)
	iverilog -o $@ $<

clean:
	-rm *.vcd *.vvp
