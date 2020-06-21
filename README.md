# pycaptcha
[![Build Status](https://travis-ci.org/bierschi/credstuffer.png?branch=master)](https://travis-ci.org/bierschi/credstuffer) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[pycaptcha](https://github.com/bierschi/pycaptcha) is a python package which tries solve different kinds of captcha:

- Solves word captcha 
- Solves math captcha
- Solves reCAPTCHA (audio, image)


## Installation

install [pycaptcha](https://pypi.org/project/pycaptcha/) with pip
<pre><code>
pip3 install pycaptcha
</code></pre>

or from source
<pre><code>
sudo python3 setup.py install
</code></pre>


## Usage and Examples

Print the available arguments for pycaptcha
<pre><code>
pycaptcha --help
</code></pre>


## Logs

logs can be found in `/var/log/pycaptcha`

## Troubleshooting
add your current user to group `syslog`, this allows the application/scripts to create a folder in
`/var/log`. Replace `<user>` with your current user
<pre><code>
sudo adduser &lt;user&gt; syslog
</code></pre>
to apply this change, log out and log in again and check with the terminal command `groups`

## Changelog
All changes and versioning information can be found in the [CHANGELOG](https://github.com/bierschi/pycaptcha/blob/master/CHANGELOG.rst)

## License
Copyright (c) 2019 Bierschneider Christian. See [LICENSE](https://github.com/bierschi/pycaptcha/blob/master/LICENSE)
for details
