SOURCES=greater_tb.v greater.v
.PHONY: all clean greater.vcd greater_tb.vvp

all: greater.vcd

greater.vcd: greater_tb.vvp
	vvp $<

greater_tb.vvp: $(SOURCES)
	iverilog -o $@ $<

clean:
	-rm *.vcd *.vvp
