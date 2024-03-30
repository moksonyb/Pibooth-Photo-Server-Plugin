
# Pibooth QR Server Plugin
``pibooth-qr-server`` is a plugin for the **[pibooth](https://pypi.org/project/pibooth/)** application.

It adds an automatic server upload functionality that integrates with the ``pibooth-qrcode`` plugin to display the generated link as a QR code and uses the ``Pibooth Photo Server`` as a backend.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/pibooth-qr-server.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pibooth-qr-server
   ```

3. Install the required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```
4. Install pibooth-qrcode if you haven't done so:
   ```bash
   pip3 install pibooth-qrcode
   ```
5. Deploy the 
   [``Pibooth Photo Server``](https://github.com/moksonyb/Pibooth-Photo-Server) and generate an access token:
   ```
   node server.js -k [Name of the token] [Expiration time in days]
   ```
   

## Configuration
*Note: _These sections _should_ be automatically added_ to the `pibooth.cfg` upon running `pibooth --configure` once.*<br>

To use the Pibooth QR Server Plugin, you need to define the following parameters in the `pibooth.cfg` file under the `[DOWNLOAD_SERVER]` section:<br>
*Note: The URL should be defined without the last "/"*
```ini
[DOWNLOAD_SERVER]
# Server URL to download the picture.
# Required by 'qr_server' plugin
server_url = <https://yourserver.example.net>

# Duration the image is available in hours for download.
# Required by 'qr_server' plugin
upload_available_hours = 24

# Token to authenticate the download server.
# Required by 'qr_server' plugin
token = <your token>
```

Additionally, you need to configure the `prefix_url` parameter under the `[QRCODE]` section in the `pibooth.cfg` file by changing it to ``{url}``:

```ini
[QRCODE]
# URL which may be composed of variables: {picture}, {count}
# Required by 'qrcode' plugin
prefix_url = {url}
```

If ``pip`` can't install the plugin properly you can also import it as a path in the `pibooth.cfg`:
```ini
[GENERAL]
...

# Path to custom plugin(s) not installed with pip (list of quoted paths accepted)
plugins = /path/to/plugin/pibooth_qr_server.py

...
```