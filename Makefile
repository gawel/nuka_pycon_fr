clean:
	rm -Rf bin/ include/ lib/

venv: clean
	virtualenv -p python3 .
	bin/pip install -r requirements.txt

impress:
	rm -Rf html
	~/py/impress/bin/impress -i rst/index.rst

serve:
	bin/python -m http.server
