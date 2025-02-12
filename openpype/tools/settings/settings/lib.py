from Qt import QtCore

# Offset of value change trigger in ms
VALUE_CHANGE_OFFSET_MS = 300


def create_deffered_value_change_timer(callback):
    """Deffer value change callback.

    UI won't trigger all callbacks on each value change but after predefined
    time. Timer is reset on each start so callback is triggered after user
    finish editing.
    """
    timer = QtCore.QTimer()
    timer.setSingleShot(True)
    timer.setInterval(VALUE_CHANGE_OFFSET_MS)
    timer.timeout.connect(callback)
    return timer
