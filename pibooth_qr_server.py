# -*- coding: utf-8 -*-

"""Pibooth plugin to download picture via qr code using the Pibooth download server."""

import pibooth
import requests
import os
from pibooth.utils import LOGGER


__version__ = "0.1.2"

from server_upload import upload_picture

SECTION = 'DOWNLOAD_SERVER'


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option(SECTION, 'server_url', 'https://<your server>',
                   "Server URL to download the picture.")
    cfg.add_option(SECTION, 'upload_available_hours', 48,
                   "Duration the image is available in hours for download.")
    cfg.add_option(SECTION, 'token', '<your_token>',
                   "Token to authenticate the download server.")


@pibooth.hookimpl
def state_processing_exit(cfg, app):
    """
    Generate the QR Code and store it in the application.
    """

    LOGGER.info("Send picture to download server...")
    app.previous_picture_url = upload_picture(app.previous_picture_file, cfg.get(SECTION, 'upload_available_hours'), cfg.get(SECTION, 'token'), cfg.get(SECTION, 'server_url'))
    LOGGER.info(f"Successfull upload! {app.previous_picture_url}")


