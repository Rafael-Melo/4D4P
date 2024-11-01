import string, secrets
import hashlib
import base64
from pathlib import Path

class FernetHasher:
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent
    KEY_DIR = BASE_DIR / 'keys'

    @classmethod
    def _get_random_string(cls, length=25):
        string = ''
        for i in range(length):
            string += secrets.choice(cls.RANDOM_STRING_CHARS)
        # print(string)

        # string = 'VoceTemCaraDeQuemOOFGratis'

        return string

    @classmethod
    def create_key(cls, archive=False):
        value = cls._get_random_string()
        print(value)
        hasher = hashlib.sha256(value.encode('utf-8')).digest()
        # print(hasher)
        key = base64.b64encode(hasher)
        # print(key)
        if archive:
            return key, cls.archive_key(key)
        return key, None

    @classmethod
    def archive_key(cls, key):
        file = 'key.key'
        while Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(length=5)}.key'
        with open(cls.KEY_DIR / file, 'wb') as arq:
            arq.write(key)
        
        return cls.KEY_DIR / file


# FernetHasher.create_key()
# print(FernetHasher.KEY_DIR)
print(FernetHasher.create_key(archive=True))