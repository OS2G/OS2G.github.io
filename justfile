# Runs the SSG script to build the site
build:
	uv run ssg.py --auto-index

# Runs the build script anytime a file in ./src changes
watch:
	watchexec -w ./src -w ./data.json -- just build

# Removes the ./www directory
clean:
	[ ! -d ./www ] || rm -r ./www

# starts a python server in ./www on 0.0.0.0:3040
serve: build
	[ -d ./www ] && uv run python -m http.server 3040 -d ./www
