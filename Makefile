# ------------------------------------------------------------------
# Makefile
# ------------------------------------------------------------------


.phony: format

setup_formatting:
		@pip install mdformat
		# @pip install mdformat-gfm
		# @pip install mdformat-gfm mdformat-frontmatter mdformat-footnote
		# @pip install mdformat-myst



format:
	@mdformat .
