# curl_cffi url decode issue
This repo is a minimal example to reproduce a bug where the python `curl_cffi` library url decodes urls before making a request.
This is causing issues when trying to make requests where a url purposefully contains a special character that should not be url decoded.

# Prerequisites
- Python 3 (I'm using version 3.9.6)
- Virtualenv (optional but recommended)

# How to run
1. Clone the repo
2. Create a virtual environment (optional but recommended)
3. Install the requirements `pip install -r requirements.txt`
4. Run the script `python app.py`

There is an assert present which should succeed with the provided url (as there are no redirects) but fails due to the url decoding issue.

```python
assert response.url == url
```

