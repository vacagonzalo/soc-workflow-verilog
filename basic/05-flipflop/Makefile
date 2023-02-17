SOURCES=flipflop_tb.v flipflop.v
.PHONY: all clean flipflop.vcd flipflop_tb.vvp

all: flipflop.vcd

flipflop.vcd: flipflop_tb.vvp
	vvp $<

flipflop_tb.vvp: $(SOURCES)
	iverilog -o $@ $<

clean:
	-rm *.vcd *.vvp
