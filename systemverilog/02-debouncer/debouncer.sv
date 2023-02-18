module debouncer #(
    parameter PRESSED = 1'b1)(
    input wire clk,
    input wire rst,
    input wire en,
    input wire i,
    output reg o);

    localparam RELEASED = !PRESSED;

    enum logic [1:0]{UP, FALLING, DOWN, RISING} state;

    always @(posedge clk or posedge rst) begin
        if(rst) begin
            state <= UP;
            o <= 1'b0;

        end else if(en) begin
            case (state)
                UP: begin
                    if(i == PRESSED)
                        state <= FALLING;
                end

                FALLING: begin
                    if(i == PRESSED) begin
                        state <= DOWN;
                        o <= 1'b1;
                    end else
                        state <= UP;
                end

                DOWN: begin
                    if(i == RELEASED) state <= RISING;
                end

                RISING: begin
                    if(i == RELEASED) begin
                        state <= UP;
                        o <= 1'b0;
                    end else
                        state <= DOWN;
                end

            endcase
        end
    end

    `ifdef COCOTB_SIM
    initial begin
    $dumpfile ("debouncer.vcd");
    $dumpvars (0, debouncer);
    #1;
    end
    `endif

endmodule
