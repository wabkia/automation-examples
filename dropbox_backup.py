import os
import getpass
from subprocess import call

# get username of logged in user and set dropbox path variable
USER_NAME = getpass.getuser()
USER_PATH = '/Users/{0}'.format(USER_NAME)
DROPBOX_PATH = '/Users/{0}/Dropbox (Project Team)'.format(USER_NAME)
LINK_DIRS = ['Desktop', 'Library', 'Documents', '.cups', '.ssh']

# os.chdir(DROPBOX_PATH)

# function to get a list of folders in dropbox_path
def get_dropbox_subdirs(dropbox_path=DROPBOX_PATH):
    if os.path.exists(dropbox_path):
        return os.listdir(dropbox_path)
    else:
        return "The Dropbox directory does not exist."

# create list of directories in the dropbox_path, check dropbox_subdir to see if
# it exists in the dropbox_path already and if it does, adds it to a list of directories
# to backup by appending '.archive' to the directory name
def get_backup_subdirs(dropbox_path=DROPBOX_PATH, link_dirs=LINK_DIRS):
    dropbox_subdirs = get_dropbox_subdirs(dropbox_path)
    
    # I don't like using the list like this. I am sure I can use another method
    # like sys,path.insert(0, subdir)
    backup_subdirs = []

    os.chdir(os.path.abspath(dropbox_path))

    for subdir in dropbox_subdirs:
        if subdir in link_dirs and os.path.isdir(subdir):
            backup_subdirs.append(subdir)
        else:
            pass

    return backup_subdirs

# backup existing dropbox LINK_DIRS
def backup_existing_link_dirs(dropbox_path=DROPBOX_PATH):

    os.chdir(os.path.abspath(dropbox_path))

    for backup_dir in get_backup_subdirs(dropbox_path):
        try:
            os.rename(backup_dir, '{0}.archive'.format(backup_dir))
            print 'Renaming {0} to {0}.archive'.format(os.path.abspath(backup_dir))
        except OSError:
            print '{0}.archive already exists in the Dropbox directory!'.format(backup_dir)

# create links
def create_symlinks(user_path=USER_PATH, dropbox_path=DROPBOX_PATH, link_dirs=LINK_DIRS):
    for link_dir in link_dirs:
        if not os.path.exists(os.path.join(dropbox_path, link_dir)):
            os.symlink(os.path.join(user_path, link_dir), os.path.join(
                dropbox_path, link_dir))
            print 'Linked {0} to Dropbox'.format(link_dir)
        else:
            print '{0} already exists!'.format(os.path.abspath(link_dir))

    return


# If running this module as a script, run script
if __name__ == "__main__":
    print '''
        Starting Dropbox Backup converstion...
        '''
    print '''
        Renaming existing user Dropbox folders to {folder}.archive
        '''
    
    backup_existing_link_dirs()

    print '''
        Creating "Backup" symlinks for user data in Dropbox folder...
        '''
    create_symlinks()

    print '''
        Symlinks created. Opening Dropbox folder in Finder...
        Please ensure folders are linked properly...
        '''

    call(["open", "-R", DROPBOX_PATH])

