PYTHON ?= python3
BACKLINK_REPORT ?= reports/backlink-lint-$(shell date +%F).md
HOOKS_DIR := .git/hooks
PRE_COMMIT_HOOK := $(HOOKS_DIR)/pre-commit
PRE_COMMIT_SOURCE := tools/hooks/pre-commit

.PHONY: help setup_formatting format backlink-check backlink-report pre-commit-check wiki-check check install-hooks uninstall-hooks

help:
	@echo "Available targets:"
	@echo "  make format            Format markdown files with mdformat"
	@echo "  make backlink-check    Run strict backlink checks across permanent notes"
	@echo "  make backlink-report   Write a full backlink lint report"
	@echo "  make pre-commit-check  Run strict backlink checks for staged markdown files"
	@echo "  make wiki-check        Run strict backlink checks"
	@echo "  make install-hooks     Install local git hooks"
	@echo "  make uninstall-hooks   Remove local git hooks installed by this repo"

setup_formatting:
		@pip install mdformat
		# @pip install mdformat-gfm
		# @pip install mdformat-gfm mdformat-frontmatter mdformat-footnote
		# @pip install mdformat-myst

format:
	@mdformat .

backlink-check:
	$(PYTHON) tools/check_backlinks.py --strict --summary

backlink-report:
	$(PYTHON) tools/check_backlinks.py --write "$(BACKLINK_REPORT)"

pre-commit-check:
	$(PYTHON) tools/check_backlinks.py --strict --staged --summary

wiki-check: backlink-check

check: wiki-check

install-hooks:
	@mkdir -p "$(HOOKS_DIR)"
	install -m 755 "$(PRE_COMMIT_SOURCE)" "$(PRE_COMMIT_HOOK)"
	@echo "Installed $(PRE_COMMIT_HOOK)"

uninstall-hooks:
	@rm -f "$(PRE_COMMIT_HOOK)"
	@echo "Removed $(PRE_COMMIT_HOOK)"
