GITHUB_URL=https://github.com/dkua/kua.io.git
BIBLIOGRAPHY_DIR=$(CURDIR)/data/bibliographies
filetype=.bib

build:
	@echo "Building kua.io"
	hugo

save:
	@echo "Saving kua.io"
	git add .
	git commit

publish:
	@echo "Publishing kua.io"
	git push origin master
	git subtree push --prefix=public $(GITHUB_URL) gh-pages

post:
	@echo "Making new Post"
	hugo new posts/$(name).md

talk:
	@echo "Making new Talk"
	hugo new talks/$(name).md

project:
	@echo "Making new Project"
	hugo new projects/$(name).md

bib:
	@echo "Converting $(BIBLIOGRAPHY_DIR)/$(target)$(filetype) to CSL JSON"
	pandoc-citeproc --bib2json $(BIBLIOGRAPHY_DIR)/$(target)$(filetype) > $(BIBLIOGRAPHY_DIR)/$(target).json
