install:
	poetry install

package-remove:
	python3 -m pip uninstall hexlet_code

package-install:
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish  --dry-run

install-games: # Для установки пакета из операционной системы используйте команду
	python3 -m pip install --user dist/*.whl.

lint:
	poetry run flake8 brain_games
