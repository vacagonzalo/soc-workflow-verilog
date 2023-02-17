PROJECTS := \
	01-mux

.PHONY: all clean $(PROJECTS)

all: $(PROJECTS)

$(PROJECTS):
	@echo "----------------"
	@echo "$@"
	$(MAKE) -C $@

clean:
	$(foreach PROJECT, $(PROJECTS), $(MAKE) -C $(PROJECT) clean;)
