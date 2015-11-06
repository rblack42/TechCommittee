BUILD_DIR	= 'docs/_build'

all:	setup

setup:
	pip install -r requirements.txt

clean:
	rm -rf docs/_build

html:
	cd docs && make html

publish:
	rsync -arvuz $(BUILD_DIR)/html/ rblack@www.co-pylit.org:html/TechCommittee/
.PHONY:	all publish clean html
