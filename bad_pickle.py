# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python
# -and-how-to-avoid-them-e19fbe265e03



# Input injection
def transcode_file( filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    # a bad idea!


# Assert statements
def access_function( user):
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh():
    def __reduce__(self):
        return
