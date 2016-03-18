# -*- encoding: utf-8 -*-

import pytest
from gunicorn.http.wsgi import Response
from gunicorn.six import BytesIO
from gunicorn.http.errors import InvalidHeader, InvalidHeaderName

try:
    import unittest.mock as mock
except ImportError:
    import mock


def test_http_inalid_response_header():
    """ tests whether http response headers are contains control chars """

    mocked_socket = mock.MagicMock()
    mocked_socket.sendall = mock.MagicMock()

    mocked_request = mock.MagicMock()
    response = Response(mocked_request, mocked_socket)

    with pytest.raises(InvalidHeader):
        response.start_response("200 OK", [('foo', 'essai\r\n')])

    response = Response(mocked_request, mocked_socket)
    with pytest.raises(InvalidHeaderName):
        response.start_response("200 OK", [('foo\r\n', 'essai')])
