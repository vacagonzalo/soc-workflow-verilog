SOURCES=hello_tb.v hello.v
.PHONY: all clean hello.vcd hello_tb.vvp

all: hello.vcd

hello.vcd: hello_tb.vvp
	vvp $<

hello_tb.vvp: $(SOURCES)
	iverilog -o $@ $<

clean:
	-rm *.vcd *.vvp
