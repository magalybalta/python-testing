test-project:
	@docker run --rm -t \
			-v $(PWD)/3-extract-override:/app:rw --entrypoint /resources/test.sh python-testing:latest

test-project-4:
	@docker run --rm -t \
			-v $(PWD)/4-fake-delegation:/app:rw --entrypoint /resources/test4.sh python-testing:latest

bash:
	@docker run -it -v $(PWD)/3-extract-override:/app:rw python-testing:latest bash


var:
	@echo $(VAR)

## Target Help ##
help:
	@printf "\033[31m%-22s %-59s %s\033[0m\n" "Target" " Help" "Usage"; \
	printf "\033[31m%-22s %-59s %s\033[0m\n"  "------" " ----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-22s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'
