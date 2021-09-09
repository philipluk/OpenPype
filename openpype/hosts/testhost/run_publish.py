import os
import sys
openpype_dir = ""
mongo_url = ""
project_name = ""
asset_name = ""
task_name = ""
ftrack_url = ""
ftrack_username = ""
ftrack_api_key = ""

host_name = "testhost"
current_file = os.path.abspath(__file__)


def multi_dirname(path, times=1):
    for _ in range(times):
        path = os.path.dirname(path)
    return path


os.environ["OPENPYPE_MONGO"] = mongo_url
os.environ["OPENPYPE_ROOT"] = multi_dirname(current_file, 4)
os.environ["AVALON_MONGO"] = mongo_url
os.environ["AVALON_PROJECT"] = project_name
os.environ["AVALON_ASSET"] = asset_name
os.environ["AVALON_TASK"] = task_name
os.environ["AVALON_APP"] = host_name
os.environ["OPENPYPE_DATABASE_NAME"] = "openpype"
os.environ["AVALON_CONFIG"] = "openpype"
os.environ["AVALON_TIMEOUT"] = "1000"
os.environ["AVALON_DB"] = "avalon"
os.environ["FTRACK_SERVER"] = ftrack_url
os.environ["FTRACK_API_USER"] = ftrack_username
os.environ["FTRACK_API_KEY"] = ftrack_api_key
for path in [
    openpype_dir,
    r"{}\repos\avalon-core".format(openpype_dir),
    r"{}\.venv\Lib\site-packages".format(openpype_dir)
]:
    sys.path.append(path)

from Qt import QtWidgets, QtCore

from openpype.tools.new_publisher.window import PublisherWindow


def main():
    """Main function for testing purposes."""
    import avalon.api
    import pyblish.api
    from openpype.modules import ModulesManager
    from openpype.hosts.testhost import api as testhost

    manager = ModulesManager()
    for plugin_path in manager.collect_plugin_paths()["publish"]:
        pyblish.api.register_plugin_path(plugin_path)

    avalon.api.install(testhost)

    app = QtWidgets.QApplication([])
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    window = PublisherWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()