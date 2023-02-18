module data_generator(
  input wire clock,
  input wire srst,
  input wire enable,
  input wire read,
  output reg [31:0] data);

  enum bit {up, down} state;

  always @(posedge clock, posedge srst) begin
    if (srst) begin
      data <= 0;
      state <= down;

    end else if (enable) begin

      case (state)
        up: begin
          if (!read) begin
            state <= down;
          end
        end

        down: begin
          if (read) begin
            state <= up;
            data <= data + 1;
          end
        end

      endcase
    end
  end

endmodule
