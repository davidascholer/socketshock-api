from datetime import datetime, timedelta

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner

from django_api.settings import CLOUDFROND_KEY_ID, CLOUDFRONT_URL, CLOUDFRONT_SECRET

def rsa_signer(message):
    key_id = CLOUDFRONT_SECRET.encode()
    private_key = serialization.load_pem_private_key(
        key_id,
        password=None,
        backend=default_backend()
    )
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())

def sign_url(uri, days = 3):
    key_id = CLOUDFROND_KEY_ID
    url = CLOUDFRONT_URL + uri
    expire_date = datetime.now() + timedelta(days=days)

    cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)

    # Create a signed url that will be valid until the specific expiry date
    # provided using a canned policy.
    signed_url = cloudfront_signer.generate_presigned_url(
        url, date_less_than=expire_date)
    return signed_url
