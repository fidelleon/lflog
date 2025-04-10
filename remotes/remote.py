from remotes.clublog import ClubLog
from remotes.eqsl import eQSL
from remotes.lotw import LoTW


def update_lotw_users():
    print('Updating LoTW users')
    LoTW.update_lotw_users()


def update_eqsl_users():
    print('Updating eQSL users')
    eQSL.update_eqsl_users()


def update_clublog_database():
    print('Updating ClubLog data')
    ClubLog.update_clublog_database()


def update_all():
    update_lotw_users()
    update_eqsl_users()
    update_clublog_database()
