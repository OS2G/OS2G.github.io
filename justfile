install: clean
	python3 -m venv ./venv
	./venv/bin/pip3 install -r ./requirements.txt

# Runs the SSG script to build the site
build:
	./venv/bin/python3 ./ssg.py --auto-index

# Runs the build script anytime a file in ./src changes
watch:
	watchexec -w ./src -- just build

# Removes the ./www directory
clean:
	[ ! -d ./www ] || rm -r ./www
	[ ! -d ./venv ] || rm -rf ./venv

# starts a python server in ./www on 0.0.0.0:3040
serve:
	[ -d ./www ] && python3 -m http.server 3040 -d ./www
