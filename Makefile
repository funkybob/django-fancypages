.PHONY: compile-static tests

STATIC_DIR="fancypages/static/fancypages/"
ifndef PYTEST_OPTS
    PYTEST_OPTS="--pep8"
endif

smaller:
	uglifyjs fancypages/static/fancypages/libs/wysihtml5/wysihtml5-config.js > fancypages/static/fancypages/libs/wysihtml5/wysihtml5-config.min.js
	uglifyjs fancypages/static/fancypages/libs/wysihtml5/wysihtml5-0.3.0.js > fancypages/static/fancypages/libs/wysihtml5/wysihtml5-0.3.0.min.js

dev:
	pip install -e .
	pip install -r requirements.txt

compile-static:
	grunt

tests: test-fancypages test-oscar-fancypages test-migration-sqlite

travis:
	${MAKE} test-fancypages
	pip install -r requirements_oscar.txt
	${MAKE} test-oscar-fancypages

test-fancypages:
	py.test ${PYTEST_OPTS}

test-oscar-fancypages:
	USE_OSCAR_SANDBOX=true py.test  ${PYTEST_OPTS}

test-migration-sqlite:
	./sandboxes/oscar_fancypages/manage.py syncdb --noinput --migrate --settings=sandbox.settings_migration_sqlite

docs:
	${MAKE} -C docs html
