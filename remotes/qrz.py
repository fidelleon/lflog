import requests
import xmltodict

from main import qrz


class QRZ:
    qrz_xml = "https://xmldata.qrz.com/xml/current/"

    @staticmethod
    def get_session_token() -> str:
        """
        Gets the QRZ API session token
        """

        answer = requests.get(f"{QRZ.qrz_xml}?username={qrz['username']}&password={qrz['password']};agent={qrz['agent']}")
        answer.raise_for_status()
        qrz_data = xmltodict.parse(answer.text)

        # Verify there were no errors
        if error_message := qrz_data['QRZDatabase']['Session'].get('Error'):
            raise Exception(error_message)

        session_key = qrz_data['QRZDatabase']['Session']['Key']
        return session_key

    @staticmethod
    def get_callsign_info(callsign: str) -> dict:
        session_token = QRZ.get_session_token()
        qrz_url = f"{QRZ.qrz_xml}?s={session_token};callsign={callsign}"
        answer = requests.get(qrz_url)
        answer.raise_for_status()
        qrz_data = xmltodict.parse(answer.text)
        print(qrz_data)

        # Verify there were no errors
        if error_message := qrz_data['QRZDatabase']['Session'].get('Error'):
            # This usually means the callsign does not exist
            return {'status': 'error',  'message': error_message}
        return {'data': qrz_data['QRZDatabase']['Callsign'], 'status': 'ok'}
