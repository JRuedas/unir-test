import http.client
from urllib.error import HTTPError
import os
import unittest
from urllib.request import urlopen
from unittest.mock import patch

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add_correct(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_fail_nan_1st_op(self):
        url = f"{BASE_URL}/calc/add/a/2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_add_fail_nan_2nd_op(self):
        url = f"{BASE_URL}/calc/add/2/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_substract_correct(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract_fail_nan_1st_op(self):
        url = f"{BASE_URL}/calc/substract/a/2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_substract_fail_nan_2nd_op(self):
        url = f"{BASE_URL}/calc/substract/2/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_multiply_correct(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_fail_nan_1st_op(self):
        url = f"{BASE_URL}/calc/multiply/a/2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_multiply_fail_nan_2nd_op(self):
        url = f"{BASE_URL}/calc/multiply/2/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_divide_correct(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_divide_fail_nan_1st_op(self):
        url = f"{BASE_URL}/calc/divide/a/2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_divide_fail_nan_2nd_op(self):
        url = f"{BASE_URL}/calc/divide/2/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_divide_fail_with_zero_division(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_power_correct(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_fail_nan_1st_op(self):
        url = f"{BASE_URL}/calc/power/a/2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_power_fail_nan_2nd_op(self):
        url = f"{BASE_URL}/calc/power/2/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_power_fail_zero_power_to_negative(self):
        url = f"{BASE_URL}/calc/power/0/-2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_sqrt_correct(self):
        url = f"{BASE_URL}/calc/sqrt/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_sqrt_fail_nan_op(self):
        url = f"{BASE_URL}/calc/sqrt/a"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_sqrt_fail_sqrt_of_negative(self):
        url = f"{BASE_URL}/calc/sqrt/-3"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_log_correct(self):
        url = f"{BASE_URL}/calc/log/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_log_fail_nan_op(self):
        url = f"{BASE_URL}/calc/log/a"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_log_fail_log_of_zero(self):
        url = f"{BASE_URL}/calc/log/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )

    def test_api_log_fail_log_of_negative(self):
        url = f"{BASE_URL}/calc/log/-1"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.status, http.client.BAD_REQUEST, f"Error en la petición API a {url}"
            )            