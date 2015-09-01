import time
from apns import APNs, Frame, Payload

cert_file = 'a_fake_cert_file.pem'
key_file = 'a_fake_key_file.pem'

apns = APNs(use_sandbox=True, cert_file=cert_file, key_file=key_file)

# Send a notification
token_hex = 'b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b87'
payload = Payload(alert='Hello World!', sound='default', badge=3)
apns.gateway_server.send_notification(token_hex, payload)

# Send multiple notifications in a signle transmission
frame = Frame()
identifier = 1
expiry = time.time() + 3600
priority = 10
frame.add_item('b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b87',
		payload, identifier, expiry, priority)
apns.gateway_server.send_notification_multiple(frame)

