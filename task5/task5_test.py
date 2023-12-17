import pytest
from PyQt5.QtCore import Qt
from task5 import MyWidget


@pytest.fixture
def app(qtbot):
    test_app = MyWidget()
    qtbot.addWidget(test_app)
    return test_app


def test_initial_state(app):
    assert not app.firstBox.isChecked()
    assert not app.secondBox.isChecked()
    assert not app.thirdBox.isChecked()
    assert not app.fourthBox.isChecked()
    assert not app.fifthBox.isChecked()
    assert not app.pushButton.isHidden()
    assert app.pushButton.isEnabled()
    assert app.pushButton.text() == "Accept"


def test_hide_button(app, qtbot):
    qtbot.mouseClick(app.fourthBox, Qt.LeftButton)

    assert app.pushButton.isHidden()


def test_show_button(app, qtbot):
    app.fourthBox.setChecked(True)
    qtbot.mouseClick(app.fourthBox, Qt.LeftButton)

    assert not app.pushButton.isHidden()


def test_disable_button(app, qtbot):
    qtbot.mouseClick(app.fifthBox, Qt.LeftButton)

    assert not app.pushButton.isEnabled()


def test_enable_button(app, qtbot):
    app.fifthBox.setChecked(True)
    qtbot.mouseClick(app.fifthBox, Qt.LeftButton)

    assert app.pushButton.isEnabled()


def test_enlarge_button(app, qtbot):
    initial_size = app.pushButton.size()
    qtbot.mouseClick(app.thirdBox, Qt.LeftButton)
    
    assert app.pushButton.size() == initial_size * 2


def test_reset_button_size(app, qtbot):
    initial_size = app.pushButton.size()
    app.thirdBox.setChecked(True)
    qtbot.mouseClick(app.thirdBox, Qt.LeftButton)

    assert app.pushButton.size() == initial_size


def test_change_button_color(app, qtbot):
    qtbot.mouseClick(app.firstBox, Qt.LeftButton)

    assert 'background-color' in app.pushButton.styleSheet()


def test_reset_button_color(app, qtbot):
    app.firstBox.setChecked(True)
    qtbot.mouseClick(app.firstBox, Qt.LeftButton)
    
    assert "background-color: #fdfdfd" in app.pushButton.styleSheet()


def test_change_button_text(app, qtbot):
    qtbot.mouseClick(app.secondBox, Qt.LeftButton)
    
    assert app.pushButton.text() == "New Text"


def test_reset_button_text(app, qtbot):
    app.secondBox.setChecked(True)
    qtbot.mouseClick(app.secondBox, Qt.LeftButton)
    
    assert app.pushButton.text() == "Accept"
