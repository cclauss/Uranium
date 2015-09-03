# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

from . import PerObjectSettingsTool

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("uranium")

def getMetaData():
    return {
        "plugin": {
            "name": "Per Object Settings Tool",
            "author": "Ultimaker",
            "version": "1.0",
            "description": i18n_catalog.i18nc("Per Object Settings plugin description", "Provides the Per Object Settings."),
            "api": 2
        },
        "tool": {
            "name": i18n_catalog.i18nc("Mirror Tool name", "Per Object Settings"),
            "description": i18n_catalog.i18nc("Per Object Settings description", "Configure per-object settings"),
            "icon": "setting_per_object",
            "tool_panel": "PerObjectSettingsPanel.qml"
        },
    }

def register(app):
    return { "tool": PerObjectSettingsTool.PerObjectSettingsTool() }
