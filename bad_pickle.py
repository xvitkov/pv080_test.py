# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python
# -and-how-to-avoid-them-e19fbe265e03

def transcode_file(filename):
    """Input injection"""
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    return command
    # a bad idea!


def access_function(user):
    """Assert statements"""
    assert user.is_admin, 'user does not have access'
    # secure code...


class RunBinSh():
    """Pickles"""
    def __reduce__(self):
        return
