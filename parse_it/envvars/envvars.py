import os
from typing import Optional


def read_envvar(envvar: str, force_uppercase: bool = True) -> Optional[str]:
    """Read an environment variable.

            Arguments:
                envvar -- name of the envvar to get the value of
                force_uppercase -- if the envvar key will be forced to be all in UPPERCASE, defaults to True
            Returns:
                the value of the envvar, None if doesn't exist
    """
    if force_uppercase is True:
        envvar = envvar.upper()
    envvar_value = os.getenv(envvar)

    if isinstance(envvar_value, str) is True:
        # this weird encode and decode is to avoid some cases where envvar get special characters escaped
        envvar_value = envvar_value.encode('latin1').decode('unicode_escape')
    return envvar_value


def envvar_defined(envvar: str, force_uppercase: bool = True) -> bool:
    """Check if an environment variable is defined.

            Arguments:
                envvar -- name of the envvar to get the value of
                force_uppercase -- if the envvar key will be forced to be all in UPPERCASE, defaults to True
            Returns:
                True if envvar is declared, False otherwise
    """
    if force_uppercase is True:
        envvar = envvar.upper()

    if envvar in os.environ:
        return True
    else:
        return False


def read_all_envvars_to_dict(force_uppercase: bool = True) -> dict:
    """Read all environment variables and return them in a dict form, if

                Arguments:
                    force_uppercase -- while counter-intuitive in the naming it means that if the environment variable
                        is uppercase the dict will treat it as the same one as a lowercase one & will return it in
                        lowercase form (name saved to match all the other uses of said function)
                Returns:
                    A dict of all environment variables key/value pairs
        """
    envvar_dict = {}
    for envvar in os.environ:
        if force_uppercase is True:
            envvar_dict[envvar.lower()] = os.environ.get(envvar)
        else:
            envvar_dict[envvar] = os.environ.get(envvar)
    return envvar_dict
