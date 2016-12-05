import virtualenv, textwrap
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess, sys
ZCBUILDOUT_VERSION='2.5.3'
# This is the latest setuptools possible for now -
# since 20.2 requires that all versions be PEP-440 compliant
SETUPTOOLS_VERSION='20.1.1'
PIP_VERSION='8.1.2'
def extend_parser(parser):
    parser.add_option(
        '--buildout_version',
        dest='buildout_version',
        default=ZCBUILDOUT_VERSION,
        help='Optional specification of zc.buildout version to use when bootstrapping')
    parser.add_option(
        '--setuptools-version',
        dest='setuptools_version',
        default=SETUPTOOLS_VERSION,
        help='Optional specification of setuptools version to use when bootstrapping')
def after_install(options, home_dir):
    if sys.platform == 'win32':
        bin = 'Scripts'
    else:
        bin = 'bin'
    # Install package example:
    #subprocess.call([join(home_dir, bin, 'easy_install'),
    #                 'MyPackage'])
    # Run script example:
    #subprocess.call([join(home_dir, bin, 'my-package-script'),
    #                 'setup', home_dir])
    if not os.path.exists(os.path.join(home_dir, 'buildout.cfg')):
        shutil.copy(os.path.join(home_dir, 'buildout.cfg.example'),
                    os.path.join(home_dir, 'buildout.cfg'))
    if os.path.exists('bootstrap-buildout.py'):
        logger.notify('')  # newline
        logger.notify('Running buildout bootstrap')
        logger.notify('zc.buildout == ' + str(options.buildout_version))
        logger.notify('setuptools == ' + str(options.setuptools_version))
        subprocess.call([os.path.join(home_dir, bin, 'python'),
                        'bootstrap-buildout.py',
                        '--buildout-version=' + options.buildout_version,
                        '--setuptools-version=' + options.setuptools_version
                        ])
        logger.notify('')  # newline
        # Fix InsecurePlatformWarning:
        subprocess.call([os.path.join(home_dir, bin, 'pip'),
                        'install', 'pyopenssl', 'ndg-httpsclient', 'pyasn1'])
        logger.notify('updating setuptools to ' + SETUPTOOLS_VERSION)
        subprocess.call([os.path.join(home_dir, bin, 'pip'),
                        'install', 'setuptools==' + SETUPTOOLS_VERSION])
        subprocess.call([os.path.join(home_dir, bin, 'pip'),
                        'install', 'pip==' + PIP_VERSION])

def adjust_options(options, args):
    options.no_wheel = True
"""))
f = open('bootstrap-virtualenv_.py', 'w').write(output)
