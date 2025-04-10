import datetime
import re
from typing import Any

from remotes.clublog import ClubLog


class Callsign:
    def __init__(self, callsign: str):
        """

        :param callsign: The QSO callsign
        """
        try:
            # Try to set it to uppercase
            self.callsign = callsign.upper()
        except AttributeError:
            raise AttributeError("Callsign must be an instance of str")

        # Validate its character set - only numbers and letters
        valid_set = re.compile(r'^\w+$')

        if not valid_set.match(self.callsign):
            raise AttributeError("Callsign can only contain alphanumeric characters")

    def get_callsign_info(self, qso_date: datetime.date = datetime.datetime.now(datetime.UTC)) -> dict[str, Any]:
        """
        Try to obtain the callsign info from the QSO callsign.

        :return:
        """
        answer = {'callsign': self.callsign,
                  'clublog_prefix': None,
                  'callsign_prefix': None,
                  }
        prefix_data = ClubLog.get_prefixes()
        if self.callsign[0] in '0123456789':
            # Numeric prefix
            match_prefix = re.compile(r'^(\d+\w+\d+\w)\w*$')
            regular_pfx = re.compile(r'^(\d+\w+\d+).+$')
        else:
            match_prefix = re.compile(r'^([A-Z]+\d+\w)\w*$')
            regular_pfx = re.compile(r'^([A-Z]+\d+)\w*$')

        if group_match := match_prefix.match(self.callsign):
            complete_group = group_match.group(1)
            answer['complete_group'] = complete_group
            while len(complete_group) > 1:
                # Loop from full length to not less than two chars
                cl_match = next((t for t in prefix_data if t['call'] == complete_group and t['start'].replace(tzinfo=datetime.UTC) <= qso_date <= t['end'].replace(tzinfo=datetime.UTC)), None)
                if cl_match:
                    answer['clublog_prefix'] = cl_match
                    break
                complete_group = complete_group[:-1]
        # Regular prefix
        regular_pfx = re.compile(r'^(\d+\w+\d+).+$')
        if group_match := regular_pfx.match(self.callsign):
            answer['callsign_prefix'] = group_match.group(1)
        return answer

    def __str__(self) -> str:
        """
        Defaults to given callsign

        :return: callsign
        """
        return self.callsign

    def __repr__(self) -> str:
        """
        Repr format

        :return: str for repr format
        """
        return f"Callsign('{self.callsign}')"
