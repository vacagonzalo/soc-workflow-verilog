SOURCES=decoder2to4_tb.v decoder.v
.PHONY: all clean decoder.vcd decoder_tb.vvp

all: decoder.vcd

decoder.vcd: decoder_tb.vvp
	vvp $<

decoder_tb.vvp: $(SOURCES)
	iverilog -o $@ $<

clean:
	-rm *.vcd *.vvp
