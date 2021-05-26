PACKAGE_DIRS = $(shell go list -f '{{ .Dir }}' ./...)
PACKAGES = $(shell go list ./...)

secrets-install:
	brew install gitleaks
	brew install pre-commit
	pre-commit install

secrets:
	gitleaks --path=. -v --repo-config-path=.git-templates/rules.toml

