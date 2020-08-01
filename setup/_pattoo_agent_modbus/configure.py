"""Configure the mobus agent."""
import os
from pattoo_shared.installation import configure, shared
from pattoo_shared import files


def install():
    """Start configuration process.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    if os.environ.get('PATTOO_CONFIGDIR') is None:
        os.environ['PATTOO_CONFIGDIR'] = '{0}etc{0}pattoo'.format(os.sep)
    config_directory = os.environ.get('PATTOO_CONFIGDIR')

    mobus_agent_dict = {
            'polling_interval': 300,
    }

    # Attempt to create configuration directory
    files.mkdir(config_directory)

    # Create the pattoo user and group
    configure.create_user('pattoo', '/nonexistent', ' /bin/false', True)

    # Attempt to change the ownership of the configuration directory
    shared.chown(config_directory)

    config_file = configure.pattoo_config(
                                        'pattoo_agent_modbustcpd',
                                        config_directory,
                                        mobus_agent_dict)

    configure.check_config(config_file, mobus_agent_dict)
