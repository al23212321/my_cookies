#!/usr/bin/env python3
"""Retrieve leetcode cookies from Chrome with local keyring"""

import sys

import click
import browser_cookie3


class _FirefoxXDG(browser_cookie3.FirefoxBased):
    """Firefox with XDG Base Directory support (Firefox 128+)."""

    def __init__(self, cookie_file=None, domain_name="", key_file=None):
        args = {
            'linux_data_dirs': [
                '~/snap/firefox/common/.mozilla/firefox',
                '~/.config/mozilla/firefox',         # XDG config path (Firefox 128+)
                '~/.local/share/mozilla/firefox',    # XDG data path (alternative)
                '~/.mozilla/firefox',
            ],
            'windows_data_dirs': [
                {'env': 'APPDATA', 'path': r'Mozilla\Firefox'},
                {'env': 'LOCALAPPDATA', 'path': r'Mozilla\Firefox'},
            ],
            'osx_data_dirs': [
                '~/Library/Application Support/Firefox',
            ],
        }
        super().__init__('Firefox', cookie_file, domain_name, key_file, **args)


def _firefox_xdg(domain_name=""):
    return _FirefoxXDG(domain_name=domain_name).load()


@click.command()
@click.option('-d', '--domain-name', help='The target domain, e.g. xxx.com')
@click.option('-k', '--keys', help='Keys to retrieve from cookies. '
'It should be the comma separated string, e.g. key1,key2,key3. If it '
'is not specified all keys will be retrieved.')
def retrieve_cookies(domain_name, keys):
    "Retrieve cookies from the domain. Print the result to stdout."
    cookiejar = None

    # For compatibility
    if not domain_name:
        domain_name = "leetcode.com"

    cookie_keys = []
    if keys and len(keys) > 0:
        cookie_keys = [k.strip() for k in keys.split(',')]

    cookie_loaders = {
        "Chrome": browser_cookie3.chrome,
        "Chromium": browser_cookie3.chromium,
        "Brave": browser_cookie3.brave,
        "Firefox": _firefox_xdg,
        "LibreWolf": browser_cookie3.librewolf,
        "Edge": browser_cookie3.edge,
        "Vivaldi": browser_cookie3.vivaldi,
        "Opera": browser_cookie3.opera,
        "Opera GX": browser_cookie3.opera_gx,
        "Arc": browser_cookie3.arc,
    }

    for browser_name, loaders in cookie_loaders.items():
        try:
            cookiejar = loaders(domain_name=domain_name)
            if cookiejar:
                break
        except Exception as e:
            print(f"Get cookie from {browser_name} failed: {e}",
                  file=sys.stderr)

    if not cookiejar or len(cookiejar) == 0:
        print("Get cookie failed, make sure you have Chrome, Chromium, Brave, "
              "Firefox, LibreWolf, Edge, Vivaldi, Opera, Opera GX, or Arc "
              "installed and logged in to the domain at least once.")
        return

    retrieve_all_keys = len(cookie_keys) == 0
    for c in cookiejar:
        if retrieve_all_keys or (c.name in cookie_keys):
            print(c.name, c.value)


def main():
    retrieve_cookies()


if __name__ == "__main__":
    main()
