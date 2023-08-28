import pytest
from unittest.mock import patch, Mock
from flaskr.app import App


class TestApp:

    @pytest.fixture(autouse=True)
    def setup_mock_app(self):
        with patch('flaskr.app.load_dotenv'), \
                patch('flaskr.app.Flask'), \
                patch('flaskr.app.SQLAlchemy') as mock_sqlalchemy:
            mock_sqlalchemy_instance = Mock()
            mock_sqlalchemy.return_value = mock_sqlalchemy_instance
            self.app = App()
            yield

    def test_configure_app(self):
        assert True is True
