module adder #(parameter DATA_WIDTH = 32)(
    input [DATA_WIDTH-1:0]A,
    input [DATA_WIDTH-1:0]B,
    input CI,
    output [DATA_WIDTH-1:0]O,
    output CO);

assign {CO, O} = A + B + CI;

endmodule
