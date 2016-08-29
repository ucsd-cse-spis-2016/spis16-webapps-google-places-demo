

To use [python-google-places](https://github.com/slimkrazy/python-google-places), you'll need to do this on ACMS:

```
pip install --user python-google-places
```

or this on your own laptop:

```
pip install python-google-places
```

# Google API Key

You need a Google API Key from the `Google Places API Web Service`

# Define your key in the env.sh file

Copy env.sh.sample to env.sh with:

```
cp env.sh.sample env.sh
```

Then edit env.sh to add a definition for GOOGLE_PLACES_API_KEY, like this:

```
export GOOGLE_PLACES_API_KEY=s8fawefj98aw9efaew89fasefa98ewf
```

Then, in each new terminal window you open, before running idle, or before using `python mywebapp.py`, you need to type this at the bash terminal prompt:

```
. env.sh
```

You can see if it worked by running the script `python env_demo.py`.   If you didn't do `. env.sh` yet, it will look like this:

```
$ python env_demo.py
GOOGLE_PLACES_API_KEY= None
GOOGLE_PLACES_API_KEY is undefined
$ 
```

Here is what it looks like when it IS defined:

```
$ python env_demo.py
GOOGLE_PLACES_API_KEY= 's8fawefj98aw9efaew89fasefa98ewf'
GOOGLE_PLACES_API_KEY=s8fawefj98aw9efaew89fasefa98ewf
$ 
```

This keeps the key value out of the Python code that gets committed into github.   Note that `env.sh` appears in the `.gitignore` for this repo, so it NOT committed to github~

# Add the import to the Python code where you are using the Google Places API:

```python
from googleplaces import GooglePlaces, types, lang
```

