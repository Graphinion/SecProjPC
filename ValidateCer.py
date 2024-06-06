import traceback
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256

def validate_certificate(certificate_path):
    try:
        with open(certificate_path, 'rb') as cert_file:
            cert_data = cert_file.read()
            try:
                cert = x509.load_pem_x509_certificate(cert_data, default_backend())
            except ValueError:
                # If loading PEM format fails, try DER format
                cert = x509.load_der_x509_certificate(cert_data, default_backend())
            # Print the signature algorithm OID
            print(f"Certificate algorithm {cert.signature_algorithm_oid.dotted_string}")
            # Check the signature algorithm OID
            if cert.signature_algorithm_oid.dotted_string == '1.2.840.113549.1.1.5':
                # This will raise an error if the certificate is not valid
                cert.public_key().verify(
                    cert.signature,
                    cert.tbs_certificate_bytes,
                    # Depending on the certificate signature algorithm
                    padding.PKCS1v15(),
                    hashes.SHA1()
                )
                print("Certificate is valid.")
                return "Certificate is valid."
            elif cert.signature_algorithm_oid.dotted_string == '1.2.840.113549.1.1.11':
                cert.public_key().verify(
                    cert.signature,
                    cert.tbs_certificate_bytes,
                    padding.PKCS1v15(),
                    SHA256()
                )
                print("Certificate is valid.")
                return "Certificate is valid."
            else:
                print("Certificate uses an unsupported signature algorithm.")
                return "Certificate uses an unsupported signature algorithm."
    except Exception as e:
        print(f"Certificate validation failed with error: {str(e)}")
        traceback.print_exc()
        return "Certificate validation failed."

# Replace 'certificate.cer' with your certificate file path
validate_certificate('/Users/aqsa/IdeaProjects/SecProjPC/certificate.crt')