PROJECTS := \
	01-hello \
	02-greater \
	03-decoder \
	04-adder \
	05-flipflop \
	06-flipflop_en

.PHONY: all clean $(PROJECTS)

all: $(PROJECTS)

$(PROJECTS):
	@echo "----------------"
	@echo "$@"
	$(MAKE) -C $@

clean:
	$(foreach PROJECT, $(PROJECTS), $(MAKE) -C $(PROJECT) clean;)
