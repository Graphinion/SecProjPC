import paramiko

def validate_ssh_key(ssh_key_path):
    try:
        key = paramiko.RSAKey(filename=ssh_key_path)
        print("SSH key is valid.")
        return "SSH key is valid."
    except IOError as e:
        print(f"Error opening SSH key file: {str(e)}")
    # retrun "Error opening SSH key file."
    except paramiko.SSHException as e:
        print(f"SSH key validation failed with error: {str(e)}")
        return "SSH key validation failed."
# Replace 'id_rsa' with your SSH key file path
validate_ssh_key('/Users/aqsa/IdeaProjects/SecProjPC/id_rsa')