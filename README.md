Lemon
-----

LED Monitor, for monitoring all sort of stuff and getting notified when something happens.

## Requirements

- WiFi
- A Raspberry Pi with a [Pimoroni Unicorn Hat HD](https://shop.pimoroni.de/products/unicorn-hat-hd)
- Raspbian on its microSD card
- A GitHub account

## Installation

On your Raspberry:

```bash
$ raspi-config nonint do_spi 0
$ reboot
$ aptitude install python3 python3-pip python3-dev python3-spidev libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev tcl8.6-dev tk8.6-dev python-tk
$ pip3 install gunicorn falcon pillow ujson unicornhathd
$ git clone https://github.com/mrusme/lemon.git
```

## Running

```bash
$ cd lemon/
$ gunicorn -b '0.0.0.0:20001' lemon:app
```

## Configuration

### GitHub Webhooks

First, make Lemon's port (e.g. `20001`) accessible from the internet. You'll probably need to add a NAT rule to your firewall/router or fire up ngrok or something like that.
Then, set up hooks on the GitHub repos (`https://github.com/mrusme/<REPO>/settings/hooks`) or organisations (`https://github.com/organizations/<ORG>/settings/hooks`) that you'd like to receive notifications for. 
For the `Payload URL`, use `http://<YOUR-DNS-NAME>:<FORWARDED-PORT>/github`. As `Content type` use `application/json`. The secret is not necessary (yet). Also, configure the webhook to `Send me everything` and don't forget to check the `Active` checkbox.
That's it. You should be receiving notifications for at least a handful of implemented GitHub events.

### IFTTT

You can create all sort of notifications using [IFTTT's Maker Webhooks](https://ifttt.com/maker_webhooks). Configuration is pretty easy:

Build your IFTTT rule by specifying the `If this` service and using `Webhooks` as `then that` service. Configure the webhook like this:

![Webhook](docs/ifttt-make_a_web_request.png)

The body of the webhook should contain of the following JSON:

```json
{ 
  "icon": "icon-name-here",
  "text": "The text to be scrolled through after the icon animation finished"
}
```

You need to make sure that the icon name you specify actually exists within the `icons/` folder and is a `.png` file. If you want to use the icon `icons/docker.png`, simply specify `"icon": "docker"` in the JSON.

## Kudos to ...

- @pimoroni for their awesome hardware
- @source-foundry for [Hack](https://github.com/source-foundry/Hack), the best Termin/Editor font there has ever been