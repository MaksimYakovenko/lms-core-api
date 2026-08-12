import pytest
from unittest import mock
import sys
import subprocess

from src.precommit.check_changes import verify_changes

def test_verify_changes_only_readme():
    with mock.patch('subprocess.run') as mock_run, mock.patch('sys.exit') as mock_exit:
        mock_run.return_value.stdout = "README.md\n"
        verify_changes()
        mock_run.assert_called_once()
        mock_exit.assert_not_called()

def test_verify_changes_other_files():
    with mock.patch('subprocess.run') as mock_run, mock.patch('sys.exit') as mock_exit:
        mock_run.return_value.stdout = "README.md\nsrc/main.py\n"
        verify_changes()
        mock_run.assert_called_once()
        mock_exit.assert_called_once_with(1)

def test_verify_changes_subprocess_error():
    with mock.patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')), mock.patch('sys.exit') as mock_exit:
        verify_changes()
        mock_exit.assert_called_once_with(1)

def test_verify_changes_unexpected_error():
    with mock.patch('subprocess.run', side_effect=Exception('Unexpected')), mock.patch('sys.exit') as mock_exit:
        verify_changes()
        mock_exit.assert_called_once_with(1)
